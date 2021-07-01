from flask import Flask, render_template, request
from flask_sqlalchemy import (SQLAlchemy)

app = Flask(__name__)


user = 'lkccpgzi'
password = 'OSxUaq-J4Nx1L_6562tvq2v-a9_BLrVm'
host = 'tuffi.db.elephantsql.com '
database = 'lkccpgzi'

app.config['SQLACHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'ProjetoDB'

db = SQLAlchemy(app)

class Organizacoes(db.Model):
  id = db.Column(db.Interger, primary_key = True)
  nome_ong = db.Column(db.String(255), nullable = False)
  url_ong = db.Column(db.String(500), nullable = False)

  def __init__(self, nome_ong, url_ong):
    self.nome_ong = nome_ong
    self.url_ong = url_ong
  
  @staticmethod
  def read_all():
    return Organizacoes.query.order_by(Organizacoes.id.asc()).all()
  
  # @staticmethod
  # def resume():
  #   return Organizacoes.query.get(registro_id)

  def save(self):
    db.session.add(self)
    db.session.commit()

@app.route('/')
def home():
  return render_template(
    'home.html',
  )

@app.route('/action')
def action():
  return render_template(
    'room.html'
  ) 

@app.route('/room/create')
def room():
  return render_template(
    'create.html',
  )

if __name__ == '__main__':
  app.run(debug = True)