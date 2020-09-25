from flask import render_template, current_app, abort, request, flash, url_for, redirect
from flask_login import login_required, current_user
from app import db
from . import main
from .forms import AddClientForm
from ..models import Client


@main.route('/')
@main.route('/index')
@login_required
def index():
    return render_template('home.html', user=current_user)


@main.route('/client/add', methods=['GET', 'POST'])
def add_client():
    form = AddClientForm()
    if form.validate_on_submit():
        new_client = Client(name=form.name.data,
                            contact_name=form.contact_name.data,
                            contact_email=form.contact_email.data,
                            user=current_user)
        db.session.add(new_client)
        db.session.commit()
        flash('New client has been created')
        return redirect(url_for('main.index'))
    return render_template('add_client.html', form=form)


@main.route('/shutdown')
def server_shutdown():
    if not current_app.testing:
        abort(404)
    shutdown = request.environ.get('werkzeug.server.shutdown')
    if not shutdown:
        abort(500)
    shutdown()
    return 'Shutting down...'
