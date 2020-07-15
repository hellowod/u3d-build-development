# -*- coding: utf-8 -*-

import datetime

def __time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def info(vars):
    print("[%s] [INFO] [SCRIPY]-%s " % (__time(), vars))

def error(vars):
    print("[%s] [ERROR] [SCRIPY]-%s " % (__time(), vars))

def warn(vars):
    print("[%s] [WARN] [SCRIPY]-%s " % (__time(), vars))