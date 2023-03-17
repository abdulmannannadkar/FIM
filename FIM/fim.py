import hashlib
import smtplib
from email.message import EmailMessage

print("Hello to File Integrity Monitor, please enter the file path of the thing you want to monitor")
filePath = input("Enter file path(ex. /home/downloads/passwords): ")
usrEmail = input("Enter your email: ")
usrPasswd = input("Enter your password that you set up in your email app password: ")
print("Make sure two factor authentication is on")
def getHash(filePath):
    md5 = hashlib.md5()
    with open(filePath,'rb') as file:
        hash = file.read()
        md5.update(hash)
        return md5.hexdigest()
def sendEmail():
    message = EmailMessage()
    message.set_content(" ")
    message['subject'] = "Someone edited one of the files on the computer"
    message['from'] = usrEmail
    message['to'] = usrEmail
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(usrEmail, usrPasswd)
    server.send_message(message)
    server.quit()
baseline = getHash(filePath)
print("[+] Just calculated your baseline")
print("[+] Checking")
while True:
    check = getHash(filePath)
    if check != baseline:
        sendEmail()
        print("[+] Someone edited the file")
        baseline = check