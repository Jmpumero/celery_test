from config.celeryconf import celery_app
from celery.schedules import crontab

from datetime import date


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):

    sender.add_periodic_task(
        7.0,
        hello.s(),
        name="task 1",
    )




@celery_app.task
def hello():
    today = date.today()
    today.strftime("%d/%m/%Y %H:%M:%S")
    return "ola k ase--->",today


@celery_app.task
def mul(x, y):
    return x * y


@celery_app.task
def xsum(numbers):
    return sum(numbers)