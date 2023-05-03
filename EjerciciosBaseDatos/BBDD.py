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
    collection_name=name #'computer science'
    collection=db[collection_name]
    return collection


def ListaHM():
        ListaHM=[]
        for x in range(1,101):
            generarGenero= random.randint(0,1)
            if generarGenero==0:
                ListaHM.append("H")
            else:
                ListaHM.append("M")
        #try:
        #    col.insert_one(ListaHM) #inserta datos en BD
       # except Exception as e: print(e)
        f=open("ListaHM", "wt", encoding='UTF-8')
        f.write(str(ListaHM)) #crea JSON
        f.close()
        return ListaHM


def retrieveAllDocuments(col):
 result=col.find({}).limit(200)
 for i in result:
        print(i)
#filtering

if __name__ == '__main__':
    client=None
    db=None
    col=None
    while 1:
        os.system("clear")
        print('1 - Conectar con Mongo')
        print('2 - Crear una  Base de datos')
        print('3 - Crear una colección')
        print('4 - Crear una lista aleatoria de 100 hombres y mujeres y guardarla')
        print('5 - Mostrar base de datos')

        print('0 - Salir')
        selection=input('Introduce el numero de la accion a realizar: ')
        if selection == '1':
            client=connectdb()
        elif selection =='2':    
            db=CreateDB("HombreYMujeres",client)    
        elif selection =='3': 
            col=createCollection('ListaHyM',db)  
        elif selection =='4': 
            lista = ListaHM()
        elif selection =='5': 
            retrieveAllDocuments(col)
        elif selection =='0':     
            break                                                               
        else:
            print('Invalid selection, try again')
        follow=input("Pres any key to continue...")
