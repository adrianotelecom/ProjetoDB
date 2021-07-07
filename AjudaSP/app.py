from operator import methodcaller
import re
from flask import Flask, render_template, request
from flask_sqlalchemy import (SQLAlchemy)

app = Flask(__name__)


user = 'lkccpgzi'
password = 'OSxUaq-J4Nx1L_6562tvq2v-a9_BLrVm'
host = 'tuffi.db.elephantsql.com'
database = 'lkccpgzi'

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

  @staticmethod
  def readSingle_ByName(nome_ong):
    return organiza.query.filter_by(nome_ong = nome_ong)

  def save(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self, new_data):
    self.nome_ong = new_data.nome_ong
    self.url_image = new_data.url_image
    self.url_ong = new_data.url_ong
    self.hotkey = new_data.hotkey

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
def details(registro_id):
  sucesso = None
  registro = organiza.read_single(registro_id)

  if request.method == 'POST':
    form = request.form
    new_data = organiza(form['nome'], form['image'], form['ong'], form['hotkey'])
    registro.update(new_data)
    sucesso = True

  return render_template(
    'update.html',
    registro = registro,
    sucesso = sucesso,
    registro_id = registro_id
  )

@app.route('/room/read/delete/<nome_ong>')
def delete(nome_ong):
  registro = organiza.readSingle_ByName(nome_ong)

  return render_template(
    'delete.html',
    registro = registro
  )

@app.route('/room/read/delete/<nome_ong>/confirmed')
def deleteConfirmed(nome_ong):
  sucesso = None
  registro = organiza.readSingle_ByName(nome_ong)

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
  