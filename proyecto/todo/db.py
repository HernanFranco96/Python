import mysql.connector
import click
from flask import current_app, g
from flask.cli import with_appcontext
from .schema import instructions

# Generamos la conexion a base de datos
def get_db():
   if 'db' not in g:
      g.db = mysql.connector.connect(
         host=current_app.config['DATABASE_HOST'],
         user=current_app.config['DATABASE_USER'],
         password=current_app.config['DATABASE_PASSWORD'],
         database=current_app.config['DATABASE'],
      )

      g.c = g.db.cursor(dictionary=True)
   return g.db, g.c

# Cerramos la conexion a base de datos
def close_db(e=None):
   db = g.pop('db', None) # Quitamos la propiedad de db a g y se la pasamos a la variable db

   if db is not None:
      db.close()

def init_db():
   db, c = get_db()

   for i in instructions:
      c.execute(i)

   db.commit()

@click.command('init-db') # Creamos una linea de comando
@with_appcontext # Nos permite acceder a las variables de entorno de get_db
def init_db_command():
   init_db()
   click.echo('Base de datos inicializada')

def init_app(app):
   app.teardown_appcontext(close_db) 
   app.cli.add_command(init_db_command)