from flask import Flask, render_template


app = Flask(__name__)


with app.app_context():
  from . import db
  db.init_app(app)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/artistas')
def artistas():
    base_de_datos = db.get_db()
    consulta = """
        SELECT name FROM artists 
        """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultados = resultado.fetchall()
    return render_template("informacion.html", artistas=lista_de_resultados)
