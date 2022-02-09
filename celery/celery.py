from celery import Celery

celery_app = Celery('project_name',
             broker='amqp://',
             backend='rpc://',
             include=['tasks.tasks'])

# Optional configuration, see the application user guide.
# app.conf.update(
#     result_expires=3600,
# )

if __name__ == '__main__':
    celery_app.start()