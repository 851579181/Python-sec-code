# -*- coding：utf-8 -*-

import importlib

def rce(cmd):
    importlib.import_module("os").system(cmd)