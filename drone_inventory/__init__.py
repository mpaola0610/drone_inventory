from flask import Flask
from config import Config
from .site.routes import site
from .authentication.routes import auth
from .api.routes import api
from .models import db as root_db, login_manager, ma
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from drone_inventory.helpers import JSONEncoder

from flask_cors import CORS
app = Flask(__name__)

app.register_blueprint(site)
app.register_blueprint(auth)
app.config.from_object(Config)
app.register_blueprint(api)

root_db.init_app(app)

migrate = Migrate(app,root_db)

login_manager.init_app(app)
login_manager.login_view = 'auth.signin' # Specify which page to load for non-authenticated users

ma.init_app(app)

app.json_encoder = JSONEncoder

CORS(app)