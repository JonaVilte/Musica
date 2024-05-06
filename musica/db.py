import sqlite3
import os
import click
from flask import current_app, g, app

db_folder = current_app.instance_path
db_name = "informacion.sqlite"
db_file = os.path.join(db_folder, db_name)
db_sql_file = "datos.sql"

def dict_factory(cursor, db_name):
    """Arma un diccionario con los valores de la fila. """
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, db_name)}



def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            db_file,
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
      # ensure the instance folder exists
    try:
        os.makedirs(current_app.instance_path)
    except OSError:
        pass

    db = get_db()

    with current_app.open_resource('datos.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)