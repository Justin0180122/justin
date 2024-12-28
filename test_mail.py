import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

#sender = 'un1931@gmail.com'  這很重要! 用變數以後不用改很多
#receiver = 'un1931@yahoo.com.tw'
#passwd = "dqna clet irtl susc"

msg = MIMEMultipart()
msg["From"] = 'un1931@gmail.com'
msg["To"] = 'un1931@yahoo.com.tw'
msg["subject"] = Header("Test send email","utf-8").encode()

#body = "This is send by python"

#a=h.encode()
#msg["subject"] = a
msg_text=MIMEText("This is send by python")
msg.attach(msg_text)
c = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=c) as server:
    server.login("un1931@gmail.com","dqna clet irtl susc")
    server.sendmail("un1931@gmail.com","un1931@yahoo.com.tw",msg.as_string())
print("success send mail!")

#with open("123.txt") as f:
#    f.writelines("hello")

#f=open("123.txt")
#f.writelines("hello")
#f.close()












#a={"key":123,"key2":456}
#a["key3"]=468
#'abc="123"+abc'
