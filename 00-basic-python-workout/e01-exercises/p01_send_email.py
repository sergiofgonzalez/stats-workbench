from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'sergio.f.gonzalez@gmail.com'
email_password = '<your-app-password-here>'

email_recipient = '<email-recipient-here>'
subject = 'My first email from Python app'
body = '''
This email has been sent from a Python app!
'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_recipient
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_recipient, em.as_string())
