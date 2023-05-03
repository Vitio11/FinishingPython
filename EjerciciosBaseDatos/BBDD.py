from pymongo.mongo_client import MongoClient
import random
import json
import os


def connectdb():
    clientDB = MongoClient('mongodb://localhost:27017/')
    db = clientDB.admin
    resultado = db.command('serverStatus')
    print('Host:',resultado['host'])
    print('Version:',resultado['version'])
    print('Process:',resultado['process'])
    print(clientDB.list_database_names())
    return clientDB

#Create a database
def CreateDB(name,clientDb):
    database_name=name 
    db=clientDb[database_name]
    return db


#Create a collection
def createCollection(name,db):
    collection_name=name 
    collection=db[collection_name]
    col=collection
    return collection


def ListaHM(col):
        ListaHM=[]
        for i in range(100):
            genero = random.choice(["H", "M"])
            ListaHM.append(genero)
            col.insert_one({"genero": genero}) # Insertar en MongoDB
        f=open("ListaHM", "wt", encoding='UTF-8')
        f.write(str(ListaHM)) #crea JSON en mi carpeta local
        f.close()
        return ListaHM


def retrieveAllDocuments(col): #muestra lo introducido
    try:
        result=col.find({}).limit(200)
        for i in result:
            print(i)
    except:
        print("Para mostrar la base de datos primero tienes que conectar con Mongo y crearla con los pasos 1,2,3 y 4")

def EstadisticasHyM():
    ListaHM=open("ListaHM",'rt', encoding='UTF-8')
    Lista=ListaHM.read()
    nH= Lista.count("H")
    nM=Lista.count("M")
    Estadisticas["Numero Hombres"]=nH
    Estadisticas["Numero Mujeres"]=nM
    Estadisticas["PorcentajeHombres"]= nH
    Estadisticas["PorcentajeMuejeres"]= nM
    for clave in Estadisticas:
        col.insert_one({clave:Estadisticas[clave]})

    print(Estadisticas)
    

if __name__ == '__main__':
    client=None
    db=None
    col=None
    Estadisticas={}
    while 1:
        os.system("clear")
        print('1 - Conectar con Mongo')
        print('2 - Crear una  Base de datos')
        print('3 - Crear una colección')
        print('4 - Crear una lista aleatoria de 100 hombres y mujeres y guardarla')
        print('5 - Mostrar base de datos')
        print('6 - Mostrar Estadisticas de las bases de datos')

        print('0 - Salir')
        selection=input('Introduce el numero de la accion a realizar: ')
        if selection == '1':
            client=connectdb()
        elif selection =='2':    
            db=CreateDB("HombreYMujeres",client)    
        elif selection =='3': 
            col=createCollection('ListaHyM',db)  
        elif selection =='4': 
            listaHM = ListaHM(col)
        elif selection =='5': 
            retrieveAllDocuments(col)
        elif selection =='6': 
            EstadisticasHyM()
        elif selection =='0':     
            break                                                               
        else:
            print('Seleccion invalida, introduce una opcion dentro de la lista')
        follow=input("Presiona cualquier tecla para continuar")
