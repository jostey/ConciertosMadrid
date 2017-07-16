import dropbox
import os

def up2drop(fname,fecha,tipo):
	token = "dpM_IFUHNt4AAAAAAABGcs_nlfWS8dYEBDEZPadD3KrSTLDLn_MMMh__dky3l1Vu"
	dbx = dropbox.client.DropboxClient(token)

	ruta = os.getcwd() + os.sep
	if tipo == 'scrapy':
		with open("madrid-"+fecha+".csv","rb") as f:
			data = f.read()
		# Eliminar csv después de almacenar en data
		# ruta = ruta + "madrid-"+fecha+".csv"
		# os.remove(ruta)
		print("Subiendo")
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

 