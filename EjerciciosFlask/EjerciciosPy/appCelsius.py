from flask import Flask, Blueprint, request, url_for
from EjerciciosPy.celsius import principal

app = Flask(__name__)

appCelsius= Blueprint('appCelsius',__name__,static_folder='static', template_folder='template' )

@appCelsius.route("/appCelsius")

def home():
    
    return f"""
        <html>
        <body>
            <h1>Grados Celsius a Farenheit</h1>
            <form method="post" action="/data">
                <label for="numero">Grados Celsius:</label>
                <input type="number" name="grados" id="grados">
                <br>
                <input type="button" value="Volver" onclick="history.back(-1)" /> 
                <input type="submit" value="Entrar">
            </form>
        </body>
        </html>
    """
@appCelsius.route('/data', methods=['POST'])

def data():
    grados=request.form["grados"]
    resultado= principal(grados)
    return f"""
        <html>
        <body>
            <h1>Grados Celsius a Farenheit</h1>
            <p>Grados Farenheit: {resultado} ºf</p>
            <input type="button" value="Volver" onclick="history.back(-1)" /> 
        </body>
        </html>
    """


if __name__ == '__main__':
   app.run(debug=True)