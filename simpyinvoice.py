import os
from app import create_app, db
from flask_migrate import Migrate, upgrade
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.cli.command()
def deploy():
    """Run deployment tasks."""
    # migrate database to latest revision
    upgrade()


@app.cli.command()
def set_up_db():
    """Create all database items. To be run before starting a test server"""
    env = os.getenv('FLASK_CONFIG')
    if env in ['test', 'dev']:
        print(f'Creating database objects in {env} environment')
        db.create_all()


@app.cli.command()
def tear_down_db():
    """Drop all database items. To be run after starting a test server"""
    env = os.getenv('FLASK_CONFIG')
    if env in ['test', 'dev']:
        print(f'Removing database objects in {env} environment')
        db.session.remove()
        db.drop_all()
