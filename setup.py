# Basic imports
import os
import sys
from os import listdir
from os.path import isfile, join
from colorama import init, Fore

import yaml
from dotenv import load_dotenv
from passlib.context import CryptContext
from sqlalchemy import create_engine
from rat_app.config import logger
from sqlalchemy.orm import sessionmaker

# Classes import
from rat_app.owner.model import Owner
from rat_app.rat.model import Rat
"""
########################################################################################################################
                                              Config
########################################################################################################################
"""
# Move base dir to the project root so we avoid relative path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Load Environment file
load_dotenv(os.path.join(BASE_DIR, ".env"))

# Crypt config
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Init Colorama
init()

# Try to load needed variables from env
DATABASE_URL = ""
try:
    DATABASE_URL = os.environ["DATABASE_URL"]
except KeyError:
    print("DATABASE_URL not defined in .env file")
    sys.exit("DATABASE_URL not defined in .env file")

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

my_path = "bootstrap/data/"
try:
    env_files = [f for f in listdir(my_path) if isfile(join(my_path, f))]
    env_choices = [str(x).split(".yaml")[0] for x in env_files]
except Exception:
    print("No env available")
    sys.exit()
if len(sys.argv) < 2:
    print(Fore.RED, "")
    print('Missing inline parameter "Environment"!')
    print("\tUsage: python setup.py <environment>")
    print(Fore.BLUE, "")
    print("Available environments are:")
    for index, item in enumerate(env_choices):
        print("\t", index, " - ", item, f"\t- example: python.py {item}")
    print(Fore.RESET, "")
    sys.exit()

environment: str = sys.argv[1]
environments = []

"""
########################################################################################################################
                                         Classes setup
########################################################################################################################
"""
with open(f"./bootstrap/data/{environment}.yaml") as file:
    try:
        conf = yaml.load(file, Loader=yaml.Loader)
        error_list: list = []

        rat = conf["rat"]
        owner = conf["owner"]

        """
        It populates the database
        """
        try:
            # Resource
            for item in owner:
                owner_object = Owner(**item)
                session.add(owner_object)
            session.commit()
        except Exception as e:
            error_list.append(f"Owner: \n{e}")

        try:
            # Resource
            for item in rat:
                rat_objet = Rat(**item)
                session.add(rat_objet)
            session.commit()
        except Exception as e:
            error_list.append(f"Rat: \n{e}")

    except Exception as e:
        error_list.append(f"Generic exception: \n{e}")

    logger.info("Setup Completed")
    print(
        Fore.CYAN,
        f"Setup Completed with {len(error_list)} errors. Check the log file:",
        Fore.BLUE,
        f"import-{environment}.log",
        Fore.RESET,
    )
    with open(f"import-{environment}.log", "w") as log_file:
        for log_line in error_list:
            log_file.writelines(log_line)
            log_file.writelines("")
