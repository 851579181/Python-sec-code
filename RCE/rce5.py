# -*- coding：utf-8 -*-
import subprocess

def rce(cmd):
    subprocess.call(["/bin/bash", "-c", cmd])