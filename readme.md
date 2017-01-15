SkyScrapper
===========

* This is a fun project to emulate the behavior of most flight trackers with the convinience that data is freshly generated and the prices reflect the true value in the market, therefore making the raw data transparent to the user

* The price check for each aeroline must be manually implemented and curated emulating the behavior of a browser, therefore new aerolines will be added incrementally  

* Prices get checked periodically to track any variation 

* The use of django server allows to expose the service in the internet

* Furthermore, alerts can be set to send a mail when the prices fall below a certain threshold

Dependencies
------------

- django (sudo pip install Django)
- celery 4.0
- pip install django-celery-beat

Run
---

- server: python manage.py runserver
- rabbitMQ (broker): sudo rabbitmq-server
- celery beat for periodic tasks: celery -A skyscrapper beat -l info -S django
- celery worker: celery -A skyscrapper worker -l info
