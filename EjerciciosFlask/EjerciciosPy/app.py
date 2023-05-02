#Mostrar una página que ponga 6 opciones: (1)

#Elejir para las 6 opciones 6 de los 20 ejercicios (DNI, Salario, Par o Impar, Celsius, etc)

#Cuando se pase a la página de la opción, se verá su funcionalidad

from flask import Flask, request, url_for

from EjerciciosPy.nmprimos import numprimos
from EjerciciosPy.celsius import celsius 
from EjerciciosPy.paroimpar import parImpar 



app = Flask(__name__)
app.register_blueprint(numprimos)
app.register_blueprint(celsius)
app.register_blueprint(parImpar)


@app.route("/")
@app.route("/home")


def home():
    
    return f"""
        <html>
        <body>
            <h1>Menu Aplicaciones HTML</h1>
            <form method="get" action="/numprimos">
                <input  type="submit" value="Ejercicio 1 -  Números Primos">
            </form>
            <form method="get" action="/celsius">
                <input  type="submit" value="Ejercicio 2 -  Calcular Grados Celsius">
            </form>
            <form method="get" action="/parImpar">
                <input  type="submit" value="Ejercicio 3 -  Determinar si es par o impar">
            </form>
        </body>
        </html>
    """


def principal():
    app.run()

if __name__ == '__main__':
   principal()


