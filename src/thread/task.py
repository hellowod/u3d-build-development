# -*- coding: utf-8 -*-

import threading
import time

class ThreadTask(threading.Thread):
    def __init__(self, method, arg):
        threading.Thread.__init__(self)
        self.method = method
        self.arg = arg

        self.thread_stoped = False

    def run(self):
        while not self.thread_stoped:
            self.method(self.arg)

    def stop(self):
        self.thread_stoped = True

    def is_stopped(self):
        return self.thread_stoped


