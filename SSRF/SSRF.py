# -*- coding：utf-8 -*-

from flask import Flask
from flask import Blueprint
from flask import request
import importlib

SSRF = Blueprint("SSRF", __name__)

@SSRF.route("/<function>/", methods=["GET"])
def ssrf(function):
    url = request.args.get("url", "")
    target = importlib.import_module("SSRF." + function)
    content = target.yds(url)

    if content:
        return content
    else:
        return "please input the url"