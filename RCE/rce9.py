# -*- coding：utf-8 -*-
import imp

def rce(cmd):
    imp.reload(__builtins__)
    __builtins__.eval(__import__("os").system(cmd))