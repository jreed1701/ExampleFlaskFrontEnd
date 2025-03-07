# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

api = Blueprint('app', 
                __name__, 
                template_folder='../templates', 
                static_folder='../static', 
                static_url_path='/app/static')

@api.route('/')
def main():
    return render_template('index.html', landingpage=True)

@api.route('/landing')
def landing():
    print('Landing content called...')
    return render_template('layout/landing.html')

@api.route('/page1')
def page1():
    #print('Page 1 Api Call triggered!')
    return render_template('api/page1.html')

@api.route('/page2')
def page2():
    #print('Page 2 Api Call triggered!')
    return render_template('api/page2.html')

@api.route('/signin')
def signin():
    return render_template('signin.html')

@api.route('/signup')
def signup():
    return render_template('signup.html')

@api.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")