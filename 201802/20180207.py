
# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.mime.text import MIMEText
textfile='abc.txt'
# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
with open(textfile) as fp:
    # Create a text/plain message
    msg = MIMEText(fp.read())

me ='dxl20@163.com'
you ='390021310@qq.com'
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = me
msg['To'] = you

username='dxl20@163.com'
passwd='a111111'
smtphost='smtp.163.com'
# Send the message via our own SMTP server.
s = smtplib.SMTP_SSL(smtphost)
s.login(username,passwd)
s.sendmail(me,you,msg.as_string())
s.quit()