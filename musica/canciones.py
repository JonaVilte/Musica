from flask import Flask, render_template, Blueprint
from . import db 

bp = Blueprint('canciones', __name__, url_prefix='/canciones')


@bp.route('/')
def cancion():
    base_de_datos = db.get_db()
    consulta = """
            SELECT name FROM tracks
            ORDER by name 	 
        """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultados = resultado.fetchall()
    pagina =  render_template("canciones.html", generos=lista_de_resultados)
    return pagina

@bp.route('/<int:id>')
def detalle(id):
    base_de_datos = db.get_db()
    consulta1 = """
        SELECT r.name, r.AlbumId FROM albums a
		JOIN tracks r on r.AlbumId = a.AlbumId
        WHERE a.AlbumId = ? ;
        """

    consulta2 = """
        SELECT a.Title FROM tracks g
        JOIN albums a ON g.AlbumId = a.AlbumId
        WHERE a.AlbumId = ? ;
        """

    resultado = base_de_datos.execute(consulta1, (id,))
    cancion = resultado.fetchone()
    resultado = base_de_datos.execute(consulta2, (id,))
    lista_de_resultados = resultado.fetchall()
    pagina = render_template("detalle_canciones.html", 
                                        cancion=cancion,
                                        canciones=lista_de_resultados)
    return pagina
