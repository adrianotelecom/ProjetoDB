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
  def resume():
    return organiza.query.get(registro_id)

  def save(self):
    db.session.add(self)
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
  registros = registros,
  # close = close,
)


if __name__ == '__main__':
  app.run(debug = True)
  