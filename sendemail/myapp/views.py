import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

files = r"Your absolute url path"
# Set up users for email
gmail_user = "youremail@gmail.com"
gmail_pwd = "yourpassword"
recipient = ['toemail@gmail.com']


# Create Module
def mail(to, subject, text, attach):
	import logging
	logging.info("logg is getting generated")
	msg = MIMEMultipart()
	msg['From'] = gmail_user
	msg['To'] = ", ".join(recipient)
	msg['Subject'] = "Error log"
	subject

	msg.attach(MIMEText(text))

	# get all the attachments
	part = MIMEBase('application', 'octet-stream')
	part.set_payload(open(files, 'rb').read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', 'attachment; filename="%s"' % files)
	msg.attach(part)

	mailServer = smtplib.SMTP("smtp.gmail.com", 587)
	mailServer.ehlo()
	mailServer.starttls()
	mailServer.login(gmail_user, gmail_pwd)
	mailServer.sendmail(gmail_user, to, msg.as_string())
	mailServer.close()


mail(recipient,
     subject="Today's report",
     text="I have attached a new generated log",
     attach=files
)

