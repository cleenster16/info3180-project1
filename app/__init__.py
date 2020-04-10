from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import random, string
x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))

app = Flask(__name__)
app.config['SECRET_KEY'] = x
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1owner:project1password123@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

app.config['UPLOAD_FOLDER'] = './app/static/images'

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views