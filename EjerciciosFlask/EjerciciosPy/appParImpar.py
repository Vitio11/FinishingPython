from flask import Flask,Blueprint, request, url_for
from EjerciciosPy.paroimpar import principal
app = Flask(__name__)

appParImpar= Blueprint('appParImpar',__name__,static_folder='static', template_folder='template' )

@appParImpar.route("/appParImpar")

def home():
    
    return f"""
        <html>
        <body>
            <h1>Determinar si es Par o Impar</h1>
            <form method="post" action="/data">
                <label for="numero">Numero:</label>
                <input type="number" name="parimpar" id="parimpar">
                <br>
                <input type="button" value="Volver" onclick="history.back(-1)" /> 
                <input type="submit" value="Entrar">
            </form>
        </body>
        </html>
    """
@appParImpar.route('/data', methods=['POST'])

def data():
    parimpar=request.form["parimpar"]
    resultado= principal(parimpar)
    return f"""
        <html>
        <body>
            <h1>Determinar si es Par o Impar</h1>
            <p>{resultado}</p>
            <input type="button" value="Volver" onclick="history.back(-1)" /> 
        </body>
        </html>
    """


if __name__ == '__main__':
   app.run(debug=True)