from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


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

if __name__ == '__main__':
  app.run(debug = True)