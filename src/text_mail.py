import getpass
import smtplib

HOST = "smtp.outlook364.com"
PORT = 587
FROM_EMAIL = "khadijamaataoui@outlook.com"
TO_EMAIL = "aregrag2005@gmail.com"
PASSWORD = getpass.getpass("Password: ")
MESSAGE = """
Subject: CSV file cleaning done alert
Hello,

The automated data pipeline has detected an anomaly in the latest processed file.
Please review the input data and take the necessary corrective action.

Regards,
Automated Monitoring System
"""

try:
    server = smtplib.SMTP(HOST, PORT)
    status_code , response = server.ehlo()
    print(f"ehlo information: \n   the status code: {status_code}\n    response:{response}\n")
    server.starttls()
    server.ehlo()

    server.login(FROM_EMAIL, "khadija123maataoui")
    print("Login OK:", status_code, response)
    server.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
    server.quit()

except Exception as e:
    print(f"Error raised:{e}")
