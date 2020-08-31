from flask import render_template
from flask_login import login_required, current_user
from . import main


@main.route('/')
@main.route('/index')
@login_required
def index():
    return render_template('home.html', user=current_user)
