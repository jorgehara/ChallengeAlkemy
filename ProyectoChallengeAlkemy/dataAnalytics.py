#dataAnalytics
import requests
import datetime



#se generan las variables de fecha para los nombres de los archivos
fecha = datetime.now()
mes=fecha.strftime('%Y-%B')
dia_mes_año=fecha.strftime('%d-%m-%Y')

#variables de los nombres de archivos
museos='museos/'+ mes 
cines='sala de cines/'+ mes 
bibliotecas='bibliotecas/'+ mes 

#comprobar si los directorios existen sino se crean
#museos
if not os.path.exists(museos):
       os.makedirs(museos)
       print ('se creo el directorio de museos porque no existia')
#cines
if not os.path.exists(cines):
       os.makedirs(cines)
       print ('se creo el directorio de cines porque no existia')
#bibliotecas
if not os.path.exists(bibliotecas):
       os.makedirs(bibliotecas)
       print ('se creo el directorio de bibliotecas porque no existia')


#guarda los datos del archivo en la variable consulta
consulta_museos = requests.get('https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museo.csv') 

consulta_cines = requests.get('https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv')

consulta_bibliotecas = requests.get('https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv')


#genera el archivo museo csv en la carpeta museos 
open(museos+'/museos-'+ dia_mes_año +'.csv', 'w', encoding='ISO-8859-1').write(consulta_museos.text)
open(cines+'/cines-'+dia_mes_año+'.csv','w' , encoding='ISO-8859-1').write(consulta_cines.text)
open(bibliotecas+'/bibliotecas'+dia_mes_año+'.csv','w',encoding='ISO-8859-1').write(consulta_bibliotecas.text)




#Crear TABLA sqlalchemy
establecer comunicacion 

from sqlalchemy import create_engine
import psycopg2

engine = create_engine('postgresql+psycopg2://postgre:D4t4b4s3@localhost:5432/datos_argentina')

conn = engine.connect()

nombres= conn.table_names()
print (nombres)

crear tablas de base datos
"crear tabla con el archivo CREARTABLADATOSUNIFICADOS"








# NCD Risk Factor Collaboration (NCD-RisC) , ht,tp://ncdrisc.org/
datos_pedidos = pd.read_csv("RUTA DE ARCHIVO.csv",encoding="ISO8851-....",)
                #engine='python')  # método para formatear los datos

datos_pedidos = datos_pedidos [['cod_localidad',
'id_provincia',
'id_departamento',
'categoría',
'provincia',
'localidad',
'nombre',
'domicilio',
'código postal',
'número de teléfono',
'mail',
'web'
]]

 for i en datos_pedidos:(
    datos_pedidos = museos, cines, bibliotecas
    #usar sql para enviar a basedatos  ()
)

datos de las colmnas enviar sql (investigar libreria dataframe to.sql)

# primeras cinco filas
bmi.head()
# primeras cinco filas de datos
bmi.head()
Procesamiento de datos
procesar_museos=pd.read_csv(museos+'/museos-'+ d_m_a +'.csv')#guarda los datos del archivo en la variable




provincias = list(procesar_museos['IdProvincia'])#convierto los valores de la columna en lista

for provincia in provincias:#leo todos los valores
    print (provincia)





