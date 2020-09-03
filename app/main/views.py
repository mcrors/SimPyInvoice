import time
from flask import render_template, current_app, abort, request
from flask_login import login_required, current_user
from . import main


@main.route('/')
@main.route('/index')
@login_required
def index():
    return render_template('home.html', user=current_user)


@main.route('/shutdown')
def server_shutdown():
    if not current_app.testing:
        abort(404)
    shutdown = request.environ.get('werkzeug.server.shutdown')
    if not shutdown:
        abort(500)
    shutdown()
    return 'Shutting down...'
