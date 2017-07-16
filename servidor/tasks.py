from celery.schedules import crontab, timedelta
from celery import Celery, task

from conciertos.conciertos.spiders.madrid import *
from drop import *
from graficas import *
from correo import *
import os
from subprocess import call
from datetime import datetime

# Crea usando RPC para devolver los datos, y el broker AMQP
app = Celery("tasks", backend="rpc://",broker="pyamqp://admin:uca@localhost//")

app.conf.beat_schedule = {
	"every-day": {
		"task": "webscraping",
		"schedule": crontab(hour=12, minute=13),
		"args": ('jostey96@gmail.com','grafica',str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))),
	}
}
app.conf.update(
	CELERY_TASK_SERIALIZE = 'pickle',
	CELERY_RESULT_SERIALIZE = 'pickle',
	accept_content = ['pickle','json']
)

app.conf.timezone = "Europe/Madrid"


@app.task(no_ack=True)
def webscraping(correo,peticion,fecha):
	os.chdir('conciertos')
	call('python3 -m scrapy crawl madrid -o ../madrid-'+fecha+'.csv',shell=True)
	os.chdir('..')
	args = uploadDropbox([correo,peticion,fecha],'scrapy')
	return args

@app.task(no_ack=True)
def make_graf(args):
	if args[0][1] == "grafica":
		plotConciertosMes(args[1],args[0][2])
		uploadDropbox(args[0],'plot')
	elif args[0][1] == "lista":
		listTop5(args[1],args[0][2])
		uploadDropbox(args[0],'plot')
	else: 
		print('Error')
		fun_correo('error',args[0])

	
	return True

def uploadDropbox(args,tipo):
	print(args)
	if tipo == 'scrapy':
		fname = "/datos_csv/madrid"
		[path,link] = up2drop(fname,args[2],'scrapy')
	elif tipo == 'plot':
		if args[1] == 'grafica':
			fname = "/datos_plot/histograma_meses"
			[path,link] = up2drop(fname,args[2],'plot')
		elif args[1] == "lista":
			fname = "/datos_list/Top5"
			[path,link] = up2drop(fname,args[2],'text')
		fun_correo(link,args[0])

	return [args,path]



	
