


# config for  celery
broker_url = 'pyamqp://'
result_backend = 'rpc://'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
enable_utc = True
task_ignore_result = True
task_routes = {'tasks.calculated.*': {'queue': 'cal'}
}

#para definir mas colas:  task_routes = {<tareas de la cola>:{queue:<nombre de la cola>}
#ejemplo:
# task_routes = {'tasks.calculated.*': {'queue': 'cal'},
# 'tasks.another.*':{'queue':'another_queue'}
# }




#timezone = 'America/Caracas'
#include = ['proj.tasks']
# Optional configuration, see the application user guide.
#celery_app.conf.task_default_routing
