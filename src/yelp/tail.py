# -*- coding: utf-8 -*-

import os
import sys
import time

class Tail(object):
    def __init__(self, tailed_file):
        self.check_file_validity(tailed_file)
        self.tailed_file = tailed_file
        self.callback = sys.stdout.write
        self.flag = True

    def follow(self, s=1):
        with open(self.tailed_file, mode='r', encoding='utf-8') as file_:
            file_.seek(0, 2)
            while True:
                curr_position = file_.tell()
                line = file_.readline()
                if not line:
                    file_.seek(curr_position)
                    time.sleep(s)
                else:
                    self.callback(line)

                if not self.flag:
                    break

    def register_callback(self, func):
        self.callback = func

    def stop(self):
        self.flag = False

    def check_file_validity(self, file_):
        if not os.access(file_, os.F_OK):
            raise TailError("file '%s' does not exist" % (file_))
        if not os.access(file_, os.R_OK):
            raise TailError("file '%s' not readable" % (file_))
        if os.path.isdir(file_):
            raise TailError("file '%s' is a directory" % (file_))

class TailError(Exception):
    def __init__(self, msg):
        self.message = msg
    def __str__(self):
        return self.message
