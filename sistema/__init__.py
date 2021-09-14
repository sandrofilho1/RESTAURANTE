from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurante.db'
app.config['SECRET_KEY'] = 'coyote'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from sistema.admin import rotas
from sistema.produtos import rotas