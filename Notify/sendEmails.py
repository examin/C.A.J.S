import configparser
import logging
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

import pandas as pd

import utils.args as args
import utils.redis_util as db

# edit data in config.ini file
config = configparser.ConfigParser()
config.read('Notify/config.ini')
Log = config['LogIn']
FROM_EMAIL = Log['email_Id']
MY_PASSWORD = Log['password']
ARG = args.argparsed


def get_users(file_name):
    names = []
    emails = []
    with open(file_name, mode='r', encoding='utf-8') as user_file:
        for user_info in user_file:
            names.append(user_info.split()[0])
            emails.append(user_info.split()[1])
    return names, emails


def parse_template(file_name):
    with open(file_name, 'r', encoding='utf-8') as msg_template:
        msg_template_content = msg_template.read()
    return Template(msg_template_content)


def main(parser_of, cve_url, new_added, cve_id, advisory):
    names, emails = get_users('Notify/contacts.txt')  # read user details
    message_template = parse_template('Notify/newcve.html')

    # set up the SMTP server
    smtp_server = smtplib.SMTP(host=ARG.smtp_address, port=ARG.smtp_port)
    smtp_server.starttls()
    if ARG.smtp_user is False:
        email_check = check_valid_email(FROM_EMAIL)
        if not email_check:
            logging.info("email id in config.ini is not valid")
            return False
        else:
            smtp_server.login(FROM_EMAIL, MY_PASSWORD)
    else:
        email_check = check_valid_email(ARG.smtp_user)
        if not email_check:
            logging.info("email id in argparse is not valid")
            return False
        else:
            smtp_server.login(ARG.smtp_user, ARG.smtp_pass)

    # Get each user detail and send the email:
    for name, email in zip(names, emails):
        multipart_msg = MIMEMultipart()  # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(
            NAME=name.title(),
            NEW_ADDED=new_added,
            CVE_LINK=cve_url,
            CVE_ID=cve_id[0],
            ADVISORY=advisory[0],
            PARSER_OF=parser_of)

        # Prints out the message body for our sake
        # print(message)

        # setup the parameters of the message
        multipart_msg['From'] = FROM_EMAIL
        multipart_msg['To'] = email
        multipart_msg['Subject'] = "New Cve Found"

        # add in the message body
        multipart_msg.attach(MIMEText(message, 'html'))

        # send the message via the server set up earlier.
        smtp_server.send_message(multipart_msg)
        del multipart_msg

    # Terminate the SMTP session and close the connection
    smtp_server.quit()


def do_need_notify(parser_of, path, cve_id, ver_affected, advisory, link):
    try:
        last_data = pd.read_csv(path)
        now_top = cve_id[0]
        first_cve = last_data['CVE-Id'].values[0]
        if now_top != first_cve:
            first_cve = last_data['CVE-Id'].values[0]
            index = 0
            new_cves=[]
            new_advisory=[]
            while cve_id[index] != first_cve and index < len(cve_id):
                new_advisory.append(advisory[index])
                new_cves.append(cve_id[index])
                index += 1
            new_added = len(new_cves)
            logging.info("Num of newly added cves in " +
                         parser_of + " is " + str(new_added))
            main(parser_of, link, new_added, new_cves, new_advisory)
            db.redis_pub(parser_of, new_cves, new_advisory, ver_affected, link)
            if new_added > 0:
                return True
        else:
            logging.info("same data as last run of " + parser_of)
            return False
    except Exception as e:
        logging.info("File error: " + " " + parser_of + " " + str(e))
        return True


def check_valid_email(addressToVerify):
    match = re.match(
        '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)
    if match is None:
        return False
    else:
        return True
