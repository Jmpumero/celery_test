from celery import Celery

celery_app = Celery('project_name',
             broker='amqp://',
             backend='rpc://',
             include=['tasks.tasks'])

# Optional configuration, see the application user guide.
celery_app.conf.update(
    result_expires=3600,
)
