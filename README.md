[*] Explicaci�n:
Cliente pide informaci�n sobre los conciertos de Madrid (petici�n: <ip_server>/index).
Puede elegir entre que le llegue una gr�fica o el "Top5 mejores precios".
Los datos son sacados por los workers mediante scrapy, son subidos a Dropbox y cuando la
tarea est� finalizada es avisado por correo.

[*] Ejecuci�n:
Ejecutar en orden Servidor, Worker(s) y por �ltimo la petici�n del Cliente.

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
Desde ah� hace las operaciones

// Fin_Cliente

