from database.firebase import authStudent
from firebase_admin import auth
from fastapi import APIRouter, Depends, HTTPException
from classes.models import User
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')
def get_curent_user(provided_token: str = Depends(oauth2_scheme)):
    decoded_token = auth.verify_id_token(provided_token)
    decoded_token['idToken'] = provided_token
    return decoded_token

@router.post('/signup', status_code=201)
async def create_acount(user: User):
    try:
        newUser = auth.create_user(**user.model_dump())
        return {'message': 'User created with id: '+newUser.uid}
    except auth.EmailAlreadyExistsError:
        raise HTTPException(status_code=409, detail='User already exists for '+user.email)

@router.post('/login')
async def create_swagger_token(user_credentials: OAuth2PasswordRequestForm = Depends()):
    try :
        user = authStudent.sign_in_with_email_and_password(email=user_credentials.username, password=user_credentials.password)
        token = user['idToken']
        print(token)
        return {
            'access_token': token,
            'token_type': 'bearer'
        }
    except :
        raise HTTPException(status_code=401, detail='Invalid credentials')

@router.get('/me')
def secure_endpoint(user_data: int = Depends(get_curent_user)):
    return user_data