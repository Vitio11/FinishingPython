#Mostrar una página que ponga 6 opciones: (1)

#Elejir para las 6 opciones 6 de los 20 ejercicios (DNI, Salario, Par o Impar, Celsius, etc)

#Cuando se pase a la página de la opción, se verá su funcionalidad

#Total de paginas HTML dinámicas: 12
#Pagina de solicitud de datos
#Pagina de resultados

from flask import Flask, request, render_template

app = Flask(__name__)

ejercicios = [
    {'id': 1, 'nombre': 'DNI', 'descripcion': 'Validación de número de DNI'},
    {'id': 2, 'nombre': 'Salario', 'descripcion': 'Cálculo de salario neto'},
    {'id': 3, 'nombre': 'Par o Impar', 'descripcion': 'Identificación de números pares o impares'},
    {'id': 4, 'nombre': 'Celsius', 'descripcion': 'Conversión de grados Celsius a Fahrenheit'},
    {'id': 5, 'nombre': 'Palíndromo', 'descripcion': 'Detección de palabras o frases palíndromas'},
    {'id': 6, 'nombre': 'Mayúsculas y minúsculas', 'descripcion': 'Conversión de texto a mayúsculas o minúsculas'}
]

@app.route('/')
def home():
    return render_template('home.html', ejercicios=ejercicios)

@app.route('/ejercicio/<int:id>')
def ejercicio(id):
    ejercicio = next((e for e in ejercicios if e['id'] == id), None)
    return render_template('ejercicio.html', ejercicio=ejercicio)

if __name__ == '__main__':
    app.run(debug=True)


