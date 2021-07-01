from flask import (Flask, render_template, request)
from sqlalchemy import SLQAlchemy
from sqlalchemy.sql.expression import true # verificar notaçaão correta do sql

app = Flask(__name__)

@app.route('/')
def home():
  return render_template(
    'home.html',
  )

if __name__ == '__main__':
  app.run(debug = True)