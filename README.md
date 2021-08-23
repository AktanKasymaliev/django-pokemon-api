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

