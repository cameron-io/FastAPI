import jwt
from app.db.user import get_user_by_public_id
from app.utils import env
from starlette.requests import HTTPConnection
from starlette.authentication import (
    AuthCredentials, AuthenticationBackend, AuthenticationError, BaseUser
)

class AuthBackend(AuthenticationBackend):
    async def authenticate(self, conn: HTTPConnection):
        token = conn.cookies.get('token')

        if token == None:
            return
        
        try:
            data = jwt.decode(token, env.getvar('SECRET_KEY'))
            return AuthCredentials(["authenticated"]), get_user_by_public_id(data['public_id'])
        except:
            return AuthenticationError('Invalid basic auth credentials')
