from flask import Flask,Blueprint, request, url_for
from EjerciciosPy.nmprimos import principal
app = Flask(__name__)

appPrimo= Blueprint('appPrimo',__name__,static_folder='static', template_folder='template' )

@appPrimo.route("/appPrimo")

def home():
    
    return f"""
        <html>
        <body>
            <h1>Numero Primo</h1>
            <form method="post" action="/data">
                <label for="numero">Numero:</label>
                <input type="number" name="primo" id="primo">
                <br>
                <input type="submit" value="Entrar">
            </form>
        </body>
        </html>
    """
@appPrimo.route('/data', methods=['POST'])

def data():
    primo=request.form["primo"]
    resultado= principal(primo)
    return f"""
        <html>
        <body>
            <h1>Numero Primo</h1>
            <p>{resultado}</p>
        </body>
        </html>
    """


if __name__ == '__main__':
   app.run(debug=True)