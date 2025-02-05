import jwt
from app.db.user import get_user_by_public_id
from app.main import app

def extract_claims_from_request(request):
    token = request.cookies['token']
    if token == None:
        None
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'])
        return get_user_by_public_id(data['public_id'])
    except:
        None
