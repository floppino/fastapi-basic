import os
import secrets
import logging
from dotenv import load_dotenv
from passlib.context import CryptContext
from pydantic import AnyHttpUrl, BaseSettings

# Azure

# Setup logger
logger = logging.getLogger("rata_app")

# Check the root project folder.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load Environment file
load_dotenv(os.path.join(BASE_DIR, ".env"))


def normalize_conf(env_key: str):
    default_values = {
        "ACCESS_TOKEN_EXPIRE_MINUTES": 90,
        "SECRET_KEY": secrets.token_urlsafe(32),
        "ALGORITHM": "HS256",
        "SERVER_NAME": "WFM",
        "SERVER_HOST": "http://localhost",
        "FRONTEND_HOST": "http:localhost:8080",
        "PROJECT_NAME": "Rats",
        "RUN_MODE": "develop",
        "CONTACT_EMAIL": "",
    }
    try:
        value = os.environ[env_key]
    except ValueError:
        print(env_key)
        if env_key in default_values:
            value = default_values[env_key]
            print(
                f"Invalid value for {env_key}, falling back to dev value: {value}"
            )
            return value
        else:
            print(f"Invalid value for {env_key} and no fallback value to apply")
            return False
    except KeyError as key_error:
        if env_key in default_values:
            value = default_values[env_key]
            print(
                f"Environment value {key_error} not found, falling back to dev value {value}"
            )
        else:
            print(f"{env_key} not in .env file and no fallback value to apply")
            return False
    return value


class Settings(BaseSettings):
    # Constants
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 14 days = 14 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 14
    ALGORITHM: str = normalize_conf("ALGORITHM")
    SERVER_NAME: str = normalize_conf("SERVER_NAME")
    FRONTEND_HOST: str = normalize_conf("FRONTEND_HOST")
    SERVER_HOST: AnyHttpUrl = normalize_conf("SERVER_HOST")
    PROJECT_NAME: str = normalize_conf("PROJECT_NAME")
    DATABASE_URL: str = normalize_conf("DATABASE_URL")
    # Objects / variables
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()