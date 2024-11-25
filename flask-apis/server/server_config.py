import os
from dotenv import load_dotenv

#to get to ensure from .env
load_dotenv(override=True)

# server secret(app secret) key and jwt secret key
SERVER_SECRET_KEY=os.getenv("APP_SECRET_KEY")
JWT_SECRET_KEY=os.getenv("JWT_SECRET_KEY")