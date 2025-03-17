import jwt
from fastapi import Request
from app.db.user import get_user_by_public_id
from app.utils import env

def extract_claims_from_request(request: Request):
    token = request.cookies.get('token')
    if token == None:
        None
    else:
        try:
            data = jwt.decode(token, env.getvar('SECRET_KEY'))
            return get_user_by_public_id(data['public_id'])
        except:
            None
