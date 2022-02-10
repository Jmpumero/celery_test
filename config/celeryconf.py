from celery import Celery

celery_app = Celery('project_name',
             broker='amqp://',
             backend='rpc://',
             #include=['tasks.another','tasks.calculated']
             )

# Optional configuration, see the application user guide.
#celery_app.conf.task_default_routing
celery_app.conf.task_routes = {'tasks.calculated.*': {'queue': 'cal'}

}