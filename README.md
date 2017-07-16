Conciertos Madrid
-----------------
-----------------

Obtención de información sobre los conciertos de Madrid mediante Web Scraping (Scrapy),
siendo de forma asíncrona y escalable (Celeris), permitiendo al usuario la obtención de
la información con una interfaz web (Bottle).

Cliente pide información sobre los conciertos de Madrid (petición: <ip_server>/index).
Puede elegir entre que le llegue una gráfica o el "Top 5 mejores precios".
Los datos son sacados por los workers mediante scrapy, son subidos a Dropbox y cuando la
tarea está finalizada es avisado por correo.

Ejecución
---------
Ejecutar en orden Servidor, Worker(s) y por último la petición del Cliente.

Servidor
* Iniciar el servicio RabbitMQ:
rabbitmq-service start

* Iniciar Flower:
flower -A tasks --broker=amqp://<user>:<pass>@localhost:5672//

* Ejecutar el servidor Bottle:
server_bottle.py

Worker(s)

* Ejecutar el worker

./startWorker.sh <num_worker>

Cliente(s)

* El cliente introduce en el navegador: <ip_server>:8080/index . Desde ahí hace las operaciones

