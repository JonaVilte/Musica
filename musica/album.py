from flask import Flask, render_template, Blueprint
from . import db 

bp = Blueprint('album', __name__, url_prefix='/album')

@bp.route('/')
def album():
    base_de_datos = db.get_db()
    consulta = """
            SELECT	Title, AlbumId from albums 
            GROUP by Title
        """
 
    resultado = base_de_datos.execute(consulta)
    lista_de_resultados = resultado.fetchall()
    pagina = render_template("album.html", albunes=lista_de_resultados)
    return pagina

@bp.route('/<int:id>')
def albunes(id):
    baseDeDatos = db.get_db()
    consulta1 = """
        SELECT Title, AlbumId FROM albums
        WHERE AlbumId = ? ;
        """
    consulta2 = """
    SELECT t.Title,r.name, r.TrackId FROM albums t
    JOIN tracks r on t.AlbumId = r.AlbumId
    WHERE t.AlbumId = ? ;
    """
    resultado = baseDeDatos.execute(consulta1, (id,))
    album = resultado.fetchone()
    resultado = baseDeDatos.execute(consulta2, (id,))
    lista_de_resultados = resultado.fetchall()
    pagina = render_template("detalle_album.html", 
                                        album=album,
                                        canciones=lista_de_resultados)
    return pagina
