# django-pokemon-api

Привет, первым делом вам нужно скопировать репозиторий.
* Скопировать репозиторий:
```
https://github.com/AktanKasymaliev/django-pokemon-api.git
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
- docker-compose up --build  
- Для миграций: docker-compose run dock_web python3 manage.py migrate
- Для создания суперпользователя: docker-compose run dock_web python3 manage.py createsuperuser
*переходи по http://127.0.0.1:8000 *
```

