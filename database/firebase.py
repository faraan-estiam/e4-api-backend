import firebase_admin
import pyrebase

from dotenv import dotenv_values
import json
env = dotenv_values(dotenv_path='.env')

if not firebase_admin._apps :
    cred = firebase_admin.credentials.Certificate(json.loads(env['FIREBASE_SERVICE_ACCOUNT_KEY']))
    firebase_admin.initialize_app(cred)

firebase = pyrebase.initialize_app(json.loads(env['FIREBASE_CONFIG']))
db = firebase.database()

#authentication
authStudent = firebase.auth()