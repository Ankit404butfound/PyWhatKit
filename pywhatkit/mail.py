import smtplib
from email.message import EmailMessage
import re
from .exceptions import UnsupportedEmailProvider


def send_mail(email_sender: str, password: str, subject: str,
              message: str, email_receiver: str) -> None:

    """Please make sure the credentials are correct"""

    domain = re.search("(?<=@)[^.]+(?=\\.)", email_sender)

    hostnames = {"gmail": "smtp.gmail.com", "yahoo": "smtp.mail.yahoo.com",
                 "outlook": "smtp.live.com", "aol": "smtp.aol.com"}

    hostname = None
    for x in hostnames:
        if x == domain.group():
            hostname = hostnames[x]
            break

    if hostname is None:
        raise UnsupportedEmailProvider(f"{domain.group()} is not supported currently!")

    with smtplib.SMTP_SSL(hostname, 465) as smtp:
        smtp.login(email_sender, password)

        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = email_sender
        msg["To"] = email_receiver
        msg.set_content(message)

        smtp.send_message(msg)
        print('Email sent Successfully!')
