# Simulacion de celery usando doble cola, con tareas programdas de forma periodica

# NOTAS:

cada conjunto de tareas programada se ubica en una carpeta en comun (tasks), con archivos propios c/u

en cada archivo se importa celery con la cofig establecidad

# EJECUCION: (se debe utilizar una consola/terminal para cada instruccion )

cada conjunto/funciones de tareas se debe ejecutar su propio worker(s) y beat(programadas)

worker para el cunjunto de tareas "calculated" definidas en: tasks/calculate.py

# celery -A tasks.calculated worker -l INFO -Q cal

tenemos que: -A {archivo de las tareas }; -Q <nombre de la cola>; -c <numero de worker>

ejemplo: celery -A tasks.calculated worker -l INFO -Q cal -c 4

la opcion -Q, es utilizada para definir la cola donde estara "esperando el worker" para este caso. La cola cal, en caso de querer agregar mas worker en la cola usamos -c <numero>

worker para el conjunto de tareas "another" definidas en: tasks/another.py

# celery -A tasks.another worker -l INFO

en este caso como no se define otra cola, el worker utilizara la cola por defecto generada por celery y 1 solo worker operara en esa cola

Para cada beat

tareas de calculated

# celery -A tasks.calculated beat -l info

tareas de another

# celery -A tasks.another beat -l info
