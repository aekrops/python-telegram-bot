import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("TOKEN"))
