from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# dados mackados
registros = [
   {
     'nome': 'Ong A',
     'uri': ''
   },
   {
     'nome': 'Ong B',
     'url': ''
   },
   {
     'nome': 'Ong C',
     'url': ''
   }
 ]


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

@app.route('/create')
def room():
  return render_template(
    'create.html',
  )

if __name__ == '__main__':
  app.run(debug = True)