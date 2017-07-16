import dropbox
import os

def up2drop(fname,fecha,tipo):
	#token = ""
	dbx = dropbox.client.DropboxClient(token)

	#user = dbx.users_get_current_account()
	ruta = os.getcwd() + os.sep
	if tipo == 'scrapy':
		with open("madrid-"+fecha+".csv","rb") as f:
			data = f.read()
		ruta = ruta + "madrid-"+fecha+".csv"
		os.remove(ruta)
		print("Subiendo")
		#fname = "/datos_csv/madrid.csv"
		fname = fname + '-' + fecha + '.csv'
	elif tipo == 'plot':
		with open("grafica-"+fecha+".png","rb") as f:
			data = f.read()
		ruta = ruta + "grafica-"+fecha+".png"
		os.remove(ruta)
		print("Subiendo")
		fname = fname + '-' + fecha + '.png'
	elif tipo == 'text':
		with open('Top5-'+fecha+'.txt',"rb") as f:
			data = f.read()
		ruta = ruta + "Top5-"+fecha+".txt"
		os.remove(ruta)
		print("Subiendo")
		fname = fname + '-' + fecha + '.txt'

	response = dbx.put_file(fname,data)
	url = dbx.share(fname)
	url = url['url']
	return [fname,url]

 
