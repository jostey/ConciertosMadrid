import socket
import re
from bottle import route, run, response, error, template, request
import threading
import logging
from datetime import datetime
from celery import chain

import tasks

logging.basicConfig( level=logging.DEBUG,
    format='[%(levelname)s] - %(threadName)-10s : %(message)s')

def hilo(email,op,date):
	logging.debug('Lanzado')
	res = chain(tasks.webscraping.s(email,op,date),tasks.make_graf.s()).delay()
	res2 = res.get()
	logging.debug('Fin')

class Conciertos:
	def __init__(self):
		pass

	def get(self, email, op, date):
		try:
			t = threading.Thread(target=hilo,args=[email,op,date])
			t.start() 
		except (KeyboardInterrupt, SystemExit):
			print("[!] Stop")
		

		return True

objeto=Conciertos()

@route('/get/<email>/<op>')
def get(email, op):
	if re.match(r"[^@]+@[^@]+\.[^@]+", email):
		date = str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
		res = objeto.get(email,op,date)
		output={'email': email,
					'error': False}
		
	else:
		output={'email': '',
					'error': True}

	return  template('get.tpl', output)

@route('/index')
def index():
	return template('form.tpl')

@route('/index', method='POST')
def do_index():
	correo = request.forms.get('correo')
	opt = request.forms.get('opt')
	if correo is None:
		return "<p>Error.</p>"
	else:
		return get(correo,opt)
        

@error(404)
def error(error):
	return template('error404.tpl')

run(host='127.0.0.1', port=8080)