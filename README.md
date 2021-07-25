# django-pokemon-api

Привет, первым делом вам нужно скопировать репозиторий.
* Скопировать репозиторий:
```
git clone https://github.com/AktanKasymaliev/online_store.git
```
* Установить все зависимости: 
```
pip install -r requirements.txt
```
* Синхронизируйте django с базой данных
```
- python manage.py makemigrations
- python manage.py migrate
```

* Create superuser
```
- python manage.py createsuperuser
```
* Наконец запустите сервер: `python3 manage.py runserver`


*Для docker-compose
```
- docker-compose build 
- docker-compose run dock_web python3 manage.py migrate
- docker-compose up
*переходи по 127.0.0.1:8000*
```

