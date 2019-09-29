# -*- coding: utf-8 -*-
from flask import Blueprint

api = Blueprint('app', __name__)

@api.route('/hello')
def hello():
    print('something happened')
    return 'Hello World'



