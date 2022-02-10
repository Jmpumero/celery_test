from config.celery import celery_app# se importa la instacia de celery
from celery.schedules import crontab

from datetime import date

#para usar el modo  "programada", se debe usar este sender
@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):

    sender.add_periodic_task(
        7.0, #pulso en segundos
        hello.s(), #nombre de la tarea a ejecutar
        name="task 1", #un nombre como identificador en el log
    )

#

#funciones/tareas
@celery_app.task
def hello():
    today = date.today()
    
    return "ola k ase--->",today.strftime("%d/%m/%Y %H:%M:%S")


@celery_app.task
def mul(x, y):
    return x * y


@celery_app.task
def xsum(numbers):
    return sum(numbers)