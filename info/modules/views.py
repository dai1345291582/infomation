from . import index_blue
from flask import render_template, current_app


@index_blue.route('/')
def index():
    return render_template('index.html')


@index_blue.route('/favicon.ico')
def web_logo():
    return current_app.send_static_file('news/favicon.ico')
