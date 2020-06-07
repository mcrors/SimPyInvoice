from flask import Response, redirect, render_template, url_for
from . import main


@main.route("/")
@main.route("/index")
def index():
    return redirect(url_for("auth.login"))
