from app.utils import env
from app.schemas.user import Register, Login
from app.db.user import get_user_by_email, create_user_account
from app.services import mail
import jwt
from datetime import datetime, timedelta, timezone

__all__ = [
    'register_user',
    'login_user'
]

def register_user(user: Register):
    account = get_user_by_email(user.email)
    if not account:
        create_user_account(
            user.name,
            user.email
        )
        return True
    else:
        return False

def login_user(user: Login):
    account = get_user_by_email(user.email)

    if not account:
        return False
    
    token_payload = {
        'public_id': account.public_id,
        'exp' : datetime.now(timezone.utc) + timedelta(minutes = 30)
    }
    token = jwt.encode(token_payload, env.getvar('SECRET_KEY'))

    mail_token(user.email, token)

    return True

def mail_token(to_addr: str, token: str):
    html = f"""
        <html>
            <body>
                <a href="{env.getvar('SERVER_URI')}/api/accounts/login?token={token}">
                    Login Link
                </a>
            </body>
        </html>
        """
    mail.send_mail(to_addr, html)
