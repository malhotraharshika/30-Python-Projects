# Python Email Sending Script

This Python script demonstrates how to send an email using the `smtplib` library with SSL encryption and the `EmailMessage` class. The script sends a basic email from one Gmail account to another.

## Code Explanation:

```python
# Import necessary modules for email handling and sending
from email.message import EmailMessage
import ssl
import smtplib

# Configure email sender, password, and recipient
sender = 'harshika.connect@gmail.com'
password = "ille jmcm cyih cmbl"
receiver = 'malhotra.harshikaa@gmail.com'

# Set email subject and body
subject = "Don't open this email"
body = """
This email is for testing!!
Don't respond to this email.
"""

# Create an EmailMessage object and set its attributes
email = EmailMessage()
email['From'] = sender
email['To'] = receiver
email['Subject'] = subject
email.set_content(body)

# Create an SSL context for secure communication with the SMTP server
context = ssl.create_default_context()

# Connect to Gmail's SMTP server using SSL, log in with sender's credentials,
# and send the email message
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver, email.as_string())
