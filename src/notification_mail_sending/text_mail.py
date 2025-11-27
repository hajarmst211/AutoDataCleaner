import getpass
import smtplib
from config.extract_statics import get_statics

mail_subtree = get_statics("mail")
HOST = "smtp.outlook364.com"
PORT = 465
FROM_EMAIL = mail_subtree["from"]
TO_EMAIL = mail_subtree["to"]
PASSWORD = getpass.getpass("Password: ")
MESSAGE = mail_subtree["message"]


'''
try:
    with smtplib.SMTP(HOST, PORT) as server:
        status_code , response = server.ehlo()
        print(f"ehlo information: \n   the status code: {status_code}\n    response:{response}\n")
        server.starttls()

        server.login(FROM_EMAIL, "khadija123maataoui")
        print("Login OK:", status_code, response)
        server.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
        server.quit()

except Exception as e:
    print(f"Error raised:{e}")
    '''

