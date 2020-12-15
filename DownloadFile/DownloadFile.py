# -*- coding：utf-8 -*-

from flask import Flask
from flask import Blueprint
from flask import request
import os
import importlib

DownloadFile = Blueprint("DownloadFile", __name__)

@DownloadFile.route("/<function>/", methods=["GET"])
def download(function):
    filename = request.args.get("filename", "")
    Down = importlib.import_module("DownloadFile." + function)

    if filename:
        return Down.yds(filename)
    else:
        return "one file named ./files/hello.txt"

