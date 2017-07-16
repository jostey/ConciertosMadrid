<html>
	<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
	<head><title>Conciertos Madrid</title></head>
	<body>
    	<div class="jumbotron">
	    	<div class="container">
				<form action="/index" method="post">
				    Correo: <input name="correo" type="text" />
				    <legend>Elige una opción:</legend>
					    <label>
					        <input type="radio" name="opt" value="grafica"> Gráfica
					    </label>
					    <label>
					        <input type="radio" name="opt" value="lista"> Top 5 Mejores Precios
					    </label>
					    <br>
					<input value="Ejecutar" type="submit" />
				</form>
			</div>
		</div>
</html>