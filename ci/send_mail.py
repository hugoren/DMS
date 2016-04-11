#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import sys,os
# import chardet




mail_host = "smtp.exmail.qq.com"
mail_user = "alert@xingren.com"
mail_pass = "6KhJg6G1"

module_dir = os.path.dirname(__file__)
file_path = os.path.join(module_dir,'command_list')
mail_content = open(file_path)


mail_to = sys.argv[1]
subject = sys.argv[2]
#content = sys.argv[3]
content = mail_content.read()
mail_content.close()
print  content

def send_mail(mail_user, mail_to, sub, content):

    # msg = MIMEText(content, _subtype='plain')
    msg = MIMEMultipart()
    msg['Subject'] = sub
    msg['From'] = mail_user
    msg['To'] = mail_to
    msg['content'] = content
    msg.attach(MIMEText(content))
    print  msg
    att = MIMEApplication(open('command_list', 'rb').read())
    att.add_header('Content-Disposition', 'attachment', filename="commlist_list.txt")
    # att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'download'
    msg.attach(att)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user, mail_pass)
        s.sendmail(mail_user, mail_to, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print e.message
        return False
if __name__ == '__main__':
    send_mail(mail_user, mail_to, subject, content.decode("ascii").encode("utf-8"))
    print  content