from info.utils.captcha.captcha import captcha
from . import index_blue
from flask import render_template, current_app


@index_blue.route('/')
def index():
    return render_template('index.html')


@index_blue.route('/favicon.ico')
def web_logo():
    return current_app.send_static_file('news/favicon.ico')


@index_blue.route('/image_code')
def image_code():
    name, text, image_code = captcha.generate_captcha()
    return image_code
