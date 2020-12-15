# -*- coding：utf-8 -*-

def rce(cmd):
    __import__("os").system(cmd)