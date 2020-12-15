# -*- coding：utf-8 -*-

from flask import Flask
from flask import Blueprint
from flask import request
import importlib

SqlInjection = Blueprint("SqlInjection", __name__)

@SqlInjection.route("/<function>/", methods=["GET"])
def sql(function):
    name = request.args.get("name", "")
    SQL = importlib.import_module("SqlInjection." + function)
    SQL.yds(name)

    return "over"