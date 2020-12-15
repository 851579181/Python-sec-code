# -*- coding：utf-8 -*-

def rce(cmd):
    execfile("/usr/lib/python2.7/os.py")
    system(cmd)