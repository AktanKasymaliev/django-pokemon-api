# django-pokemon-api

Hello first step is cloning rep:
* Clone repos:
```
https://github.com/AktanKasymaliev/django-pokemon-api.git
```
* Install all requirements: 
```
pip install -r requirements.txt
```
* Create a file settings.ini on self project level, copy under text, and add your value: 
```
[SYSTEM]
DJANGO_KEY = $key$
DEBUG = True
[DATABASE]
PASSWORD = password
USER = user
NAME = dbName
HOST=localhost
PORT=5432
```
* This project working on Postgresql, so install him:
```
sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev postgres postgres-contrib (MacOS) / 
sudo apt-get install postgresql postgresql-contrib (Ubuntu)
sudo -u postgres psql
```
* Enter in your postgresql, and create database:
```
sudo -u postgres psql
CREATE DATABASE <database name>;
CREATE USER <database user> WITH PASSWORD 'your_super_secret_password';
ALTER ROLE <database user> SET client_encoding TO 'utf8';
ALTER ROLE <database user> SET default_transaction_isolation TO 'read committed';
ALTER ROLE <database user> SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE <database name> TO '<database user>';
```
* Sync database
```
- python manage.py makemigrations
- python manage.py migrate
```

* Create superuser
```
- python manage.py createsuperuser
```
* Last one is run: `python3 manage.py runserver`


* For docker users:
```
- docker-compose up --build  
- Migrations: docker-compose run dock_web python3 manage.py migrate
- Create superuser: docker-compose run dock_web python3 manage.py createsuperuser
* redirect to http://127.0.0.1:8000 *
```

