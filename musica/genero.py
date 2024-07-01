from flask import Flask, render_template, Blueprint
from . import db 

bp = Blueprint('genero', __name__, url_prefix='/genero')

@bp.route('/')
def generos():
    base_de_datos = db.get_db()
    consulta = """
        SELECT name, GenreId FROM genres
        ORDER BY GenreId ASC	 
        """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultados = resultado.fetchall()
    pagina =  render_template("genero.html", generos=lista_de_resultados)
    return pagina

@bp.route('/<int:id>')
def detalle(id):
    base_de_datos = db.get_db()
    consulta = """
        SELECT  t.name as nombre, t.GenreId FROM genres t
		JOIN tracks g on t.GenreId=g.GenreId	
        WHERE t.GenreId = ?		 
        """



    resultado = base_de_datos.execute(consulta, (id,))
    generos = resultado.fetchone()

    pagina = render_template("detalle_genero.html", 
                                        genero=generos)
    return pagina
