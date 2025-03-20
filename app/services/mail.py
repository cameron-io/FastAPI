from app.utils import env
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

__all__ = [
    'send_mail'
]

def send_mail(to_addr: str, html: str) -> None:
    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = env.getvar('EMAIL_SENDER')
    message["To"] = to_addr

    mime_html = MIMEText(html, "html")
    message.attach(mime_html)

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(
            env.getvar('EMAIL_HOST'),
            int(env.getvar('EMAIL_PORT'))
        )

        server.starttls(context=context)

        server.login(
            env.getvar('MAILTRAP_SANDBOX_USER'),
            env.getvar('MAILTRAP_SANDBOX_PASSWORD')
        )

        server.sendmail(
            env.getvar('EMAIL_SENDER'),
            to_addr,
            message.as_string()
        )
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()
