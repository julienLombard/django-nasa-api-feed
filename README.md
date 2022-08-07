# django-nasa-api-feed
NASA feed app 

## Prerequisite
- Python should be installed in your system
- pip installation

### 1. Clone repository

### 2. Create virtual environment in django-nasa-feed-app folder

- In command line interface, run in django-nasa-feed-app folder

run "python -m venv env"

- active environnement

on Windows : run "env\Scripts\activate"

on Linux : run "source env/bin/activate"

("deactivate" to desactive it, later)

### 3. Install Django and packages

run "pip install django"

run "pip install request"

run "pip install python-decouple"

### 4. Create .env file in django-nasa-feed-app\feedproject\feedproject folder

- go to https://djecrety.ir/ to generate a Django secret key

- then, write the key in the first line of .env file, as follow: 

SECRET_KEY = 'django-insecure-YOUR_KEY_HERE'

### 5. Run local server

run  "python manage.py runserver" 

- go to the server link in the command line interface

(ctrl + c to escape server, later)

