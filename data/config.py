import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("TOKEN"))

FIREBASE_CONFIG = str(os.getenv("FIREBASE"))

firebaseConfig = {
    "apiKey": str(os.getenv("apiKey")),
    "authDomain": str(os.getenv("authDomain")),
    "databaseURL": str(os.getenv("databaseURL")),
    "projectId": str(os.getenv("projectId")),
    "storageBucket": str(os.getenv("storageBucket")),
    "messagingSenderId": str(os.getenv("messagingSenderId")),
    "appId": str(os.getenv("appId")),
    "measurementId": str(os.getenv("measurementId"))
}
