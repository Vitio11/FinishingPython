from pymongo.mongo_client import MongoClient
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
    database_name=name #'Students'
    db=clientDb[database_name]
    return db
















def GenerarListaGenero(self): #para crear la lista random de hombres y mujeres
        print('Creando lista...')
        for x in range(1,101):
            generarGenero= random.randint(0,1)
            if generarGenero==0:
                self.listaElementos.append("H")
            else:
                self.listaElementos.append("M")
        print('Lista creada satisfactoriamente.')
        print('Creando fichero...')
        self.CreacionFichero()