from typing import Union
from app.main import app
from app.utils.env import getvar
from app.db.user import get_user_by_email, create_user_account
from app.dto.user import Login, Register
from app.services.mail import send_mail
from fastapi import Response
import jwt
from datetime import datetime, timedelta, timezone

def mail_token(to_addr: str, token: str):
    html = f"""
        <html>
            <body>
                <a href="http://localhost:5000/api/accounts/login?token={token}">Login Link</a>
            </body>
        </html>
        """
    send_mail(to_addr, html)

@app.post("/register")
async def register(payload: Register, response: Response):
    account = get_user_by_email(payload.email)
    if not account:
        create_user_account(
            payload.name,
            payload.email
        )
        response.status_code = 201
        return {
            'success': 'Successfully registered.'
        }
    else:
        response.status_code = 400
        return {
            'error': 'This email is already registered to an account. Please Log in.'
        }

@app.post("/login")
async def login(payload: Login, response: Response):
    account = get_user_by_email(payload.email)
    if not account:
        response.headers['WWW-Authenticate'] = 'Basic realm ="Account does not exist"'
        response.status_code = 201
        return {
            'error': 'Account not registered.'
        }

    token_payload = {
        'public_id': account.public_id,
        'exp' : datetime.now(timezone.utc) + timedelta(minutes = 30)
    }
    token = jwt.encode(token_payload, getvar('SECRET_KEY'))

    mail_token(payload.email, token)

    response.status_code = 200
    return {
        "msg": "Check your inbox!"
    }
