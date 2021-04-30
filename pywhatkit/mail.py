import smtplib
from email.message import EmailMessage


def send_mail(email_sender: str, password: str, subject: str,
              message: str, email_receiver: str, hostname: str = 'smtp.gmail.com') -> None:

    """You can find the SMTP hostname of your service by searching on Google"""

    with smtplib.SMTP_SSL(hostname, 465) as smtp:
        smtp.login(email_sender, password)

        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = email_sender
        msg["To"] = email_receiver
        msg.set_content(message)

        smtp.send_message(msg)
        print('Email sent Successfully!')
