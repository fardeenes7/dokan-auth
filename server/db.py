from firebase_admin import credentials, firestore, initialize_app, auth
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Initialize Firestore
DEBUG = False if os.getenv("DEBUG") == "False" else True

FIREBASE_CRED = os.getenv("FIREBASE_SERVICE_ACCOUNT_KEY") if not DEBUG else os.path.join(BASE_DIR,"service-account.json")

cred = credentials.Certificate(FIREBASE_CRED)
firebase = initialize_app(cred)
db = firestore.client()