import firebase_admin
from configs.firebase_config import firebaseConfig
import pyrebase

if not firebase_admin._apps :
    cred = firebase_admin.credentials.Certificate("configs/my-api-99db8-firebase-adminsdk-qebp2-445fda4e3e.json")
    firebase_admin.initialize_app(cred)

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()