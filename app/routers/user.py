from fastapi import APIRouter
from app.schemas.user import Login, Register
from app.services import user
from fastapi import Response

router = APIRouter(
    prefix="/api/accounts",
    tags=["accounts"],
    responses={404: {"description": "Not found"}},
)

@router.post("/register")
async def register(payload: Register, response: Response):
    if user.register_user(payload) == True:
        response.status_code = 201
        return {
            'success': 'Successfully registered.'
        }
    else:
        response.status_code = 400
        return {
            'error': 'This email is already registered to an account. Please Log in.'
        }

@router.post("/login")
async def login(payload: Login, response: Response):
    if not user.login_user(payload):
        response.headers['WWW-Authenticate'] = 'Basic realm ="Account does not exist"'
        response.status_code = 201
        return {
            'error': 'Account not registered.'
        }
    
    response.status_code = 200
    return {
        "msg": "Check your inbox!"
    }
