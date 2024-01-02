from email.message import EmailMessage
import ssl
import smtplib

# email configuration
sender = 'abc@gmail.com'
password = "sender_app_password"
receiver = 'xyz@gmail.com'

# email content
subject = "Don't open this email"
body = """
This email is for testing!!
Don't respond to this email.
"""

# creating EmailMessage object
email = EmailMessage()
email['From'] = sender
email['To'] = receiver
email['Subject'] = subject
email.set_content(body)

# SSL context creation
context = ssl.create_default_context()

# Sending email using SMTP
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver, email.as_string())
