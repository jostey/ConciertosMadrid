<html>
	<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <head><title>Conciertos Madrid</title></head>
    <body>
    	<div class="jumbotron">
	    	<div class="container">
	  			<h1><span class="glyphicon glyphicon-music" aria-hidden="true"></span> Conciertos Madrid </h1>
	  				% if error:
	    			<p><span class="glyphicon glyphicon-remove" aria-hidden="true"></span> El correo es incorrecto.</p>
	    			<p>Inténtelo de nuevo con un correo válido.</p>
	    			% else:
					<p><span class="glyphicon glyphicon-ok" aria-hidden="true"></span> La tarea se est&aacute; llevando acabo en estos momentos.</p>
					<p>Cuando finalice, ser&aacute; avisado al correo: {{email}}</p>
					% end
			</div>
		</div>
    	      
    </body>
</html>

