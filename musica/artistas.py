from flask import Flask, redirect, render_template, Blueprint, request, url_for
from . import db 

bp = Blueprint('artista', __name__, url_prefix='/artistas')

@bp.route('/')
def artistas():
    base_de_datos = db.get_db()
    consulta = """
        SELECT name, ArtistId FROM artists 
        """
 
    resultado = base_de_datos.execute(consulta)
    lista_de_resultados = resultado.fetchall()
    pagina = render_template("artista.html", artistas=lista_de_resultados)
    return pagina

@bp.route("/<int:id>")
def detalle(id):
    base_de_datos = db.get_db()
    consulta1 = """
        SELECT Name, ArtistId FROM artists
        WHERE ArtistId = ? ;
    """
    consulta2 = """
        SELECT a.name, g.Title, g.AlbumId FROM albums g
        JOIN artists a ON g.ArtistId = a.ArtistId
        WHERE a.ArtistId = ? ;
    """
    resultado = base_de_datos.execute(consulta1, (id, ))
    artista = resultado.fetchone()
    resultado = base_de_datos.execute(consulta2, (id, ))
    lista_albums = resultado.fetchall()
    pagina = render_template("detalle_artista.html",
                             artista = artista,
                             albums = lista_albums)
    return pagina

@bp.route('/new', methods = ('GET','POST'))
def nuevo():
    if request.method == 'POST':
        name=request.form['name']
        
        con=db.get_db()
        consulta="""
          INSERT INTO artists ('name')
          VALUES (?)  
        """ 
        con.execute(consulta,(name,))
        con.commit()
        return redirect(url_for('artista.artistas'))

    else: 
        pagina = render_template('nuevo_actor.html')
        return pagina