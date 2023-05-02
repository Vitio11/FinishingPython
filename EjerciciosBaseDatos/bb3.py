import random
from pymongo import MongoClient

# Conectar a la base de datos de MongoDB
client = MongoClient()
db = client.test

# Crear una colección llamada "personas"
personas = db.personas


 def GenerarListaGenero(self):
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