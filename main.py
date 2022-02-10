#no hace falta este main....
from .config.celeryconf import celery_app

from celery import Celery
from celery.schedules import crontab

celery_app = Celery()


if __name__ == '__main__':
    celery_app.start()