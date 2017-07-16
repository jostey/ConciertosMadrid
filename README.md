[*] Explicación:
Cliente pide información sobre los conciertos de Madrid (petición: <ip_server>/index).
Puede elegir entre que le llegue una gráfica o el "Top5 mejores precios".
Los datos son sacados por los workers mediante scrapy, son subidos a Dropbox y cuando la
tarea está finalizada es avisado por correo.

[*] Ejecución:
Ejecutar en orden Servidor, Worker(s) y por último la petición del Cliente.

// Servidor

* Iniciar el servicio RabbitMQ:
rabbitmq-service start

* Iniciar Flower:
flower -A tasks --broker=amqp://<user>:<pass>@localhost:5672//

* Ejecutar el servidor Bottle:
server_bottle.py

// Fin_Servidor

// Worker(s)

* Ejecutar el worker

./startWorker.sh <num_worker>


// Fin_Worker

// Cliente(s)

El cliente introduce en el navegador: <ip_server>:8080/index
Desde ahí hace las operaciones

// Fin_Cliente

