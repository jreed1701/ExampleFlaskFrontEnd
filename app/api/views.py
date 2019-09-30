# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

api = Blueprint('app', 
                __name__, 
                template_folder='../templates', 
                static_folder='../static', 
                static_url_path='/app/static')

@api.route('/')
def main():
    return render_template('index.html')

@api.route('/signin')
def signin():
    return render_template('signin.html')

@api.route('/signup')
def signup():
    return render_template('signup.html')

@api.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")