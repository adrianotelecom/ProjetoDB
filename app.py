from flask import Flask, render_template, request
from flask_sqlalchemy import (SQLAlchemy)
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)


user = os.environ.get("user")
password = os.environ.get("password")
host = os.environ.get("host")
database = os.environ.get("database")

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'ProjetoDB'

db = SQLAlchemy(app)

class organiza(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  nome_ong = db.Column(db.String(255), nullable = False)
  url_image = db.Column(db.String(255), nullable = False)
  url_ong = db.Column(db.String(255), nullable = False)
  hotkey = db.Column(db.String(255), nullable = False)

  def __init__(self, nome_ong, url_image, url_ong, hotkey):
    self.nome_ong = nome_ong
    self.url_image = url_image
    self.url_ong = url_ong
    self.hotkey = hotkey
  
  @staticmethod
  def read_all():
    return organiza.query.order_by(organiza.id.asc()).all()
  
  @staticmethod
  def read_single(registro_id):
    return organiza.query.get(registro_id)

  def save(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self, newData):
    self.nome_ong = newData.nome_ong
    self.url_image = newData.url_image
    self.url_ong = newData.url_ong
    self.hotkey = newData.hotkey

    self.save()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

@app.route('/')
def home():
  return render_template(
    'home.html',
  )

@app.route('/room')
def action():
  return render_template(
    'room.html'
  ) 

@app.route('/room/create', methods = ("GET", "POST"))
def signUp():
  id_atribuido = None

  if request.method == 'POST':
    form = request.form
    registro = organiza(form['nome'], form['image'], form['ong'], form['hotkey'])
    registro.save()
    id_atribuido = registro.id

  return render_template(
    'create.html',
    id_atribuido = id_atribuido
  )

@app.route('/room/read')
def partners():
  registros =  organiza.read_all()
  return render_template(
    'read.html',
    registros = registros
)

@app.route('/room/read/update/<registro_id>', methods = ('GET', 'POST'))
def update(registro_id):
  sucesso = None
  registro = organiza.read_single(registro_id)

  if request.method == 'POST':
    form = request.form

    newData = organiza(form['nome'], form['image'], form['ong'], form['hotkey'])
    registro.update(newData)
    sucesso = True

  return render_template(
    'update.html',
    registro = registro,
    sucesso = sucesso
  )

@app.route('/room/read/delete/<registro_id>')
def delete(registro_id):
  registro = organiza.read_single(registro_id)

  return render_template(
    'delete.html',
    registro = registro
  )

@app.route('/room/read/delete/<registro_id>/confirmed')
def deleteConfirmed(registro_id):
  sucesso = None
  registro = organiza.read_single(registro_id)

  if registro:
    registro.delete()
    sucesso = True
  
  return render_template(
    'delete.html',
    registro = registro,
    sucesso = sucesso
  )


if __name__ == '__main__':
  app.run(debug = True)
  