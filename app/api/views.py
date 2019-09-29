# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from .content import Content

api = Blueprint('app', __name__, template_folder='../templates', static_folder='../static')

TOP_DICT = Content()

@api.route('/')
def main():
    return render_template('main.html')

@api.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")