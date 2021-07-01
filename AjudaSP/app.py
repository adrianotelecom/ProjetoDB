from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

user = 'lkccpgzi'
password = 'OSxUaq-J4Nx1L_6562tvq2v-a9_BLrVm'
host = 'tuffi.db.elephantsql.com'
database = 'lkccpgzi'

app.config['SQLACHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'ProjetoDB'

db = SQLAlchemy(app)

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