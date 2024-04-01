from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.auth.routes import auth_bp
from app.blog.routes import blog_bp
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(blog_bp, url_prefix='/blog')

