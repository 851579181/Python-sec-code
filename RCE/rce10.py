# -*- coding：utf-8 -*-
import sys

def rce(cmd):
    sys.modules['os'] = "/usr/lib/python2.7/os.py"
    __import__("os").system(cmd)