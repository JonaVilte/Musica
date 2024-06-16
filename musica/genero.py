from flask import Flask, render_template, Blueprint
from . import db 

bp = Blueprint('genero', __name__, url_prefix='/genero')

@bp.route('/')
def generos():
    base_de_datos = db.get_db()
    consulta = """
        SELECT name, genreId FROM genres
        ORDER BY genreId ASC	 
        """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultados = resultado.fetchall()
    pagina =  render_template("genero.html", generos=lista_de_resultados)
    return pagina

@bp.route('/<int:id>')
def detalle(id):
    base_de_datos = db.get_db()
    consulta = """
        SELECT name FROM genres 
        WHERE genreid = ?		 
        """

    consulta2 = """
        SELECT c.name from genres t
        JOIN tracks c on t.GenreId = c.GenreId
        WHERE t.GenreId	= ?
        """

    resultado = base_de_datos.execute(consulta, (id,))
    genero = resultado.fetchone()
    resultado = base_de_datos.execute(consulta2, (id,))
    lista_de_resultados = resultado.fetchall()
    pagina = render_template("detalle_genero.html", 
                                        genero=genero,
                                        canciones=lista_de_resultados)
    return pagina
