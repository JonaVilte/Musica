from flask import Flask, render_template, Blueprint
from . import db 

bp = Blueprint('genero', __name__, url_prefix='/genero')

@bp.route('/')
def artistas():
    base_de_datos = db.get_db()
    consulta = """
        SELECT t.name, b.name from artists t
        JOIN albums a on t.ArtistId = a.ArtistId
        JOIN tracks g on a.AlbumId = g.AlbumId
        JOIN genres b on g.GenreId = b.GenreId 
        """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultados = resultado.fetchall()
    pagina =  render_template("informacion.html", artistas=lista_de_resultados)
    return pagina
