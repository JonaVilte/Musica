from flask import Flask, render_template, Blueprint
from . import db 

bp = Blueprint('artista', __name__, url_prefix='/artistas')

@bp.route('/')
def artistas():
    base_de_datos = db.get_db()
    consulta = """
        SELECT name FROM artists 
        """
 
    resultado = base_de_datos.execute(consulta)
    lista_de_resultados = resultado.fetchall()
    pagina = render_template("informacion.html", artistas=lista_de_resultados)
    return pagina

