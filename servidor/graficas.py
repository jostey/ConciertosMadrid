import numpy as np
import pylab as pl
import csv
import dropbox
import codecs
import os

def plotConciertosMes(link,fecha):
	token = "dpM_IFUHNt4AAAAAAABGcs_nlfWS8dYEBDEZPadD3KrSTLDLn_MMMh__dky3l1Vu"
	dbx = dropbox.client.DropboxClient(token)

	f, metadata = dbx.get_file_and_metadata(link)
	print(link)
	out = open('temp-'+fecha+'.csv', 'wb')
	out.write(f.read())
	out.close()
	
	tabla = []
	with open('temp-'+fecha+'.csv','r') as f:
		for fila in csv.reader(f):
		    tabla.append(fila)
	f.close()
	ruta = os.getcwd() + os.sep
	ruta = ruta + "temp-"+fecha+".csv"
	os.remove(ruta)

	print(len(tabla))
	y = np.zeros((len(tabla))).tolist()
	colum = tabla[0].index('date')

	for fila in range(1,len(tabla)):
		if(tabla[fila][colum][7:len(tabla[fila][colum])] == "may"):
			y[fila] = 1
		else: 
			if(tabla[fila][colum][7:len(tabla[fila][colum])] == "jun"):
				y[fila] = 2
			else: 
				if(tabla[fila][colum][7:len(tabla[fila][colum])] == "jul"):
					y[fila] = 3
				else:
					y[fila] = 4
			
	pl.hist(y,4,(1,5))
	pl.title("Número de Conciertos en cada mes")
	pl.xticks(np.arange(4)+1.5,["Mayo","Junio","Julio","Múltiples\n Fechas"])
	pl.savefig("grafica-"+fecha+".png")

def listTop5(link,fecha):
	token = "dpM_IFUHNt4AAAAAAABGcs_nlfWS8dYEBDEZPadD3KrSTLDLn_MMMh__dky3l1Vu"
	dbx = dropbox.client.DropboxClient(token)

	f, metadata = dbx.get_file_and_metadata(link)
	out = open('temp-'+fecha+'.csv', 'wb')
	out.write(f.read())
	out.close()
	
	tabla = []
	with open('temp-'+fecha+'.csv','r') as f:
		i = 0
		for fila in csv.reader(f):
			if fila[2] is not '':
				tabla.append(fila)
			i = i+1
	f.close()
	ruta = os.getcwd() + os.sep
	ruta = ruta + "temp-"+fecha+".csv"
	os.remove(ruta)

	colum_title = tabla[0].index('title')
	colum_date = tabla[0].index('date')
	colum_price = tabla[0].index('price')
	colum_site = tabla[0].index('site')

	tab_order = sorted(tabla, key=lambda tabla: tabla[colum_price])

	with(open('Top5-'+fecha+'.txt','w')) as f:
		f.write('\t\tTOP 5 MEJORES PRECIOS\n\n')
		for i in range(1,6):
			f.write(str(tab_order[i][colum_title])+'\n\t Fecha: '+str(tab_order[i][colum_date])+'\n\t Precio: '+str(tab_order[i][colum_price])+'\n\t Sitio: '+str(tab_order[i][colum_site])+'\n\n')

	f.close()