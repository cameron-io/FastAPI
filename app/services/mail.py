from app.utils import env
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

__all__ = [
    'send_mail'
]

def send_mail(to_addr: str, html: str) -> None:
    message = MIMEMultipart("alternative")
    message["Subject"] = env.getvar('SERVER_NAME') + " team <no-reply@mail.com>"
    message["From"] = env.getvar('EMAIL_SENDER')
    message["To"] = to_addr

    mime_html = MIMEText(html, "html")
    message.attach(mime_html)

    # Try to log in to server and send email
    with smtplib.SMTP(
            env.getvar('EMAIL_HOST'),
            int(env.getvar('EMAIL_PORT'))
        ) as server:
        server.starttls()

        server.login(
            env.getvar('MAILTRAP_SANDBOX_USER'),
            env.getvar('MAILTRAP_SANDBOX_PASSWORD')
        )

        server.sendmail(
            env.getvar('EMAIL_SENDER'),
            to_addr,
            message.as_string()
        )
