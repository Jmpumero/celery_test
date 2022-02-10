from celery import Celery

celery_app = Celery("algo")
celery_app.config_from_object("config.celeryconfig")
celery_app.conf.task_routes = {'tasks.calculated.*': {'queue': 'cal'}}


