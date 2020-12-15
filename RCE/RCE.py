# -*- coding：utf-8 -*-

from flask import Flask
from flask import Blueprint
from flask import request
import importlib

RCE = Blueprint("RCE", __name__)

@RCE.route("/<function>/", methods=["GET"])
def rce(function):
    cmd = request.args.get("cmd", "")
    rce = importlib.import_module("RCE." + function)
    rce.rce(cmd)

    try:
        rce.rce(cmd)
        return "over"
    except:
        return "something wrong"

