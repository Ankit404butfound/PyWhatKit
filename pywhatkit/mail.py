import smtplib
from .exceptions import InvalidEmailService
from email.message import EmailMessage


def send_mail(email_sender: str, password: str, subject: str,
              message: str, email_receiver: str, service: str = 'gmail') -> None:
    """Supported service names are gmail, aol, outlook, yahoo"""

    if service.lower() not in ["gmail", "aol", "outlook", "yahoo"]:
        raise InvalidEmailService("Service not supported")

    hostnames = {"gmail": "smtp.gmail.com", "yahoo": "smtp.mail.yahoo.com",
                 "outlook": "smtp.live.com", "aol": "smtp.aol.com"}

    with smtplib.SMTP_SSL(hostnames[service], 465) as smtp:
        smtp.login(email_sender, password)

        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = email_sender
        msg["To"] = email_receiver
        msg.set_content(message)

        smtp.send_message(msg)
        print('Email sent Successfully!')
