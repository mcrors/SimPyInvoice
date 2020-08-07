from flask import Response, redirect, render_template, url_for
from flask_login import login_required
from . import main


@main.route('/')
@main.route('/index')
@login_required
def index():
    return render_template('home.html')
