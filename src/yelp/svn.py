# -*- coding: utf-8 -*-

import os

def update(username, password, url):
    svn_cmd = "svn up '%s' --username %s --password %s --no-auth-catch" % (url, username, password)
    print("cmd: %s" % svn_cmd)
    return os.system(svn_cmd) == 0

def revert():
    pass

def cleanup():
    pass
