#!/usr/bin/python3
from flask import Blueprint


app_apis = Blueprint('app_apis', __name__, url_prefix='/api')


from api.mvp.views.food import *
from api.mvp.views.recipe import *
from api.mvp.views.ingredient import *
