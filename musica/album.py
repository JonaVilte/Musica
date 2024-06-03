from flask import Flask, render_template, Blueprint
from . import db 

bp = Blueprint('album', __name__, url_prefix='/album')

@bp.route('/')
def album():
    base_de_datos = db.get_db()
    consulta = """
            SELECT	a.Title from artists t
            JOIN albums a on t.ArtistId = a.ArtistId
            GROUP by a.Title
        """
 
    resultado = base_de_datos.execute(consulta)
    lista_de_resultados = resultado.fetchall()
    pagina = render_template("album.html", albunes=lista_de_resultados)
    return pagina
