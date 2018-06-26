import smtplib
import configparser

from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# edit data in config.ini file 
config = configparser.ConfigParser()
config.read('config.ini')
Log = config['LogIn']
FROM_EMAIL = Log['email_Id']
MY_PASSWORD = Log['password']

def get_users(file_name):
    names = []
    emails = []
    with open(file_name , mode='r', encoding='utf-8') as user_file:
        for user_info in user_file:
            names.append(user_info.split()[0])
            emails.append(user_info.split()[1])
    return names, emails

def parse_template(file_name):
    with open(file_name, 'r', encoding='utf-8') as msg_template:
        msg_template_content = msg_template.read()
    return Template(msg_template_content)

def main(parser_of,cve_url,new_added,cve_id,advisory):
    names, emails = get_users('Notify/contacts.txt') # read user details
    message_template = parse_template('Notify/newcve.html')

    # set up the SMTP server
    smtp_server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    smtp_server.starttls()
    smtp_server.login(FROM_EMAIL, MY_PASSWORD)

    # Get each user detail and send the email:
    for name, email in zip(names, emails):
        multipart_msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(NAME=name.title(),NEW_ADDED=new_added,CVE_LINK=cve_url,CVE_ID=cve_id,ADVISORY=advisory,PARSER_OF=parser_of)


        # Prints out the message body for our sake
        #print(message)

        # setup the parameters of the message
        multipart_msg['From']=FROM_EMAIL
        multipart_msg['To']=email
        multipart_msg['Subject']="New Cve Found"

        # add in the message body
        multipart_msg.attach(MIMEText(message, 'html'))

        # send the message via the server set up earlier.
        smtp_server.send_message(multipart_msg)
        del multipart_msg

    # Terminate the SMTP session and close the connection
    smtp_server.quit()
