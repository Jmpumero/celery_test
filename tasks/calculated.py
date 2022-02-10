
from config.celery import celery_app
from celery.schedules import crontab

from datetime import date

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):

    sender.add_periodic_task(
        2,
        add.s(3,4),
        name="task_2",
    )
@celery_app.task
def add(x, y):
    return x + y


# @celery_app.task
# def mul(x, y):
#     return x * y


# @celery_app.task
# def xsum(numbers):
#     return sum(numbers)