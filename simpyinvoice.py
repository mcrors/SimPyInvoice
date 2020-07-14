import os
from app import create_app, db
from flask_migrate import Migrate

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)
