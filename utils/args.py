
import argparse
def get_args():
    parser = argparse.ArgumentParser()
    output_options = parser.add_argument_group("Output data as excel or json ref:C.A.J.S/Output/*")
    email_options = parser.add_argument_group("Email Options")
    smtp_options = parser.add_argument_group("SMTP options")


    email_options.add_argument("-a", "--sendToAll", dest="to_address", help="Send Email to all address in contacts",default=False, type=str)
    email_options.add_argument("-f", "--from", dest="from_address", help="Change sender email id account to send email from",default=False, type=str)
    email_options.add_argument("-n", "--from_name", dest="from_name", help="Add From name", default=False, type=str)
    smtp_options.add_argument("-s", "--server", dest="smtp_address",
                              help="SMTP server address (default of Gmail)", default="smtp.gmail.com",  type=str)
    smtp_options.add_argument("-p", "--port", dest="smtp_port", type=int, help="SMTP server port (default 587)",
                              default=587)
    smtp_options.add_argument("--user", dest="smtp_user", help="SMTP username",
                              default=None, type=str)
    smtp_options.add_argument("--pass", dest="smtp_pass", help="SMTP password",  type=str,
                              default=None)
    output_options.add_argument("-d", "--Data_output", dest="output_as", help="choose csv excel or json", default=False, choices=['cve', 'excel', 'json'], type=str)
    output_options.add_argument("-L", dest="output_at", help="(Default om root folder of project)", default=False, type=str)
    return parser.parse_args()
argparsed=get_args()
def main():
    print(argparsed.to_address)
    print(argparsed.from_address)
    print(argparsed.smtp_address)
    print(argparsed.smtp_port)
    print(argparsed.smtp_user)
    print(argparsed.smtp_pass)
    print(argparsed.output_as)
    print(argparsed.from_name)


    # do check if email and password is in ini or got form cli


# parser = argparse.ArgumentParser(description='The tool can trace down any new public CVE on every JWS and JBCS related upstream project.')
# parser.add_argument('-a', action="store_true", default=False)
# parser.add_argument('-b', action="store", dest="b", type=int)
# parser.add_argument('-c', action="store", dest="c", type=int)
#
# print(parser.parse_args(['-a', '-bval', '-c', '3']))
if __name__ == '__main__':
    main()
