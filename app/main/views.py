from flask import Response, redirect, render_template, url_for
from . import main


@main.route("/")
@main.route("/index")
def index():
    return Response("<HTML>Hi</HTML>")
