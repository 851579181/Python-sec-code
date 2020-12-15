# -*- coding：utf-8 -*-
import os

def rce(cmd):
    os.popen(cmd)