# Rat project

## Project

Rat is a tutorial project for the new recruits.

___

## Installation



### Requirements

To run the application you need an environment with:

- Python >= 3.8.x
- virtualenv or virtualenv wrapper
- Docker/Docker-Compose or a Postgresql Database instance



### Environment setup

Clone the repository:
```bash
$ git clone <rat-repository>.git
```

Enter the folder:
```bash
$ cd fastapi-tutorial
```

Create a virtual environment according to the requirements (or use the Pycharm settings to crete a Project Interpreter):
```bash
$ virtualenv venv
```

Create the database using docker-compose or the psql command line:
1) Using docker-compose command:
```bash
$ docker-compose -f bootstrap/docker-compose.yaml up -d
```
2) Using psql CLI:
```bash
$ sudo -u postgres psql
postgres=# create database <db-name>; 
```

Create a .env file with the required info:
```bash
$ cat <<EOF >.env
# Database
DATABASE_URL = postgresql+psycopg2://postgres:postgres@127.0.0.1:5455/<db-name>
#oAuth2 config
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 90
EOF
```

Activate the virtual environment:
```bash
$ source venv/bin/activate
```

Install the python requirements:
```bash
$ pip install -r requirements.txt
```

Execute database migration:
```bash
# For Windows
$ .\bootstrap\bin\migrate.bat
# For Unix
$ ./bootstrap/bin/migrate.sh  
```

Populate the database with the bootstrap_data.yaml (if present):
```bash
$ python setup.py test
```

Start the server via Uvicorn:
```bash
$ uvicorn main:app --reload
```
___
## Database kill and fill

In case you need to destroy, create and populate the database:
1. Delete the version file under `alembic/versions`, it is recognizable by a series of alphanumeric characters ending with `.py` extension.
2. Delete the database:
```bash
# For Windows
$ docker-compose -f bootstrap\docker-compose.yaml down -v
# For Unix
$ docker-compose -f bootstrap/docker-compose.yaml down -v
```
3. Create the database:
```bash
# For Windows
$ docker-compose -f bootstrap\docker-compose.yaml up -d
# For Unix
$ docker-compose -f bootstrap/docker-compose.yaml up -d
```
4. Execute the database migration:
```bash
# For Windows
$ bootstrap\bin\migrate.bat
# For Unix
$ ./bootstrap/bin/migrate.sh  
```
5. Populate the database with the info from the `bootstrap/data` files:
```bash
$ python setup.py test
```
___

## Setup Git Hooks

To ensure code quality and prevent bad commits we are releasing "pre-commit" git hooks.
To activate them just run the following command once:

```bash
$ git config core.hooksPath .githooks
```

Git will reformat and lint your code before every commit.

**Formatter**: black

**Linter**: flake8
___

## [WIP] Run unit tests

Execute the following command to run the test suite:

```bash
$ pytest --html=report.html  --self-contained-html 
```

Click on the generated html file to view a full report on your browser.
