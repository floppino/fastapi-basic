import os
import sys

from dotenv import load_dotenv

# Move base dir to the project root so we avoid relative path
from sqlalchemy import create_engine, text

# Models
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(BASE_DIR, ".env"))
sys.path.append(BASE_DIR)

# Load Environment file
load_dotenv(os.path.join(BASE_DIR, ".env"))

DATABASE_URL = ""
try:
    DATABASE_URL = os.environ["DATABASE_URL"]
    engine = create_engine(DATABASE_URL)
except KeyError:
    sys.exit("DATABASE_URL not defined in .env file")

with engine.begin() as conn:
    conn.execute(text("DROP schema public cascade"))

with engine.begin() as conn:
    conn.execute(text("create schema public"))
