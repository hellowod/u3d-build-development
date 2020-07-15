# -*- coding: utf-8 -*-

import platform
import time
import fileinput
import subprocess
import os
import sys
import threading
import time

import yelp.tail
import thread.task

import log.logger

def tail_thread(tail_file):
    global t
    log.logger.info("wait for tail file ... %s" % tail_file)

    while True:
        if os.path.exists(tail_file):
            log.logger.info("start tail file..... %s" % tail_file)
            break

    t = yelp.tail.Tail(tail_file)
    t.register_callback(tail_log_callback)
    t.follow()

def tail_log_callback(txt):
    print(txt, end='')

def build(method_name, unity_path, project_path, build_type, runner_type, configure, export_path, archive_path, log_path, androidjdk, androidsdk, androidndk, keystore, keystorepass, keyaliasname, keyaliaspass, il2cpp):
    str(method_name).strip()
    str(unity_path).strip()
    str(project_path).strip()
    str(build_type).strip()
    str(runner_type).strip()
    str(configure).strip()
    str(export_path).strip()
    str(archive_path).strip()
    str(log_path).strip()
    str(androidjdk).strip()
    str(androidsdk).strip()
    str(androidndk).strip()
    str(keystore).strip()
    str(keystorepass).strip()
    str(keyaliasname).strip()
    str(keyaliaspass).strip()
    str(il2cpp).strip()

    build_cmd = [unity_path, 
    '-quit', '-batchmode', 
    '-projectPath', project_path,
    '-executeMethod', method_name,
    '-b', build_type,
    '-r', runner_type,
    '-c', configure,
    '-e', export_path,
    '-a', archive_path,
    '-j', androidjdk,
    '-s', androidsdk,
    '-n', androidndk,
    '-ks', keystore,
    '-ksp', keystorepass,
    '-kan', keyaliasname,
    '-kap', keyaliaspass,
    '-i', il2cpp,
    '-logFile', log_path]

    log.logger.info('unity running cmd %s' % build_cmd)

    if os.path.exists(log_path):
        os.remove(log_path)
        log.logger.info('delete log file %s' % log_path)

    tt = thread.task.ThreadTask(tail_thread, log_path)
    tt.start()

    process = subprocess.Popen(
        build_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=project_path
    )

    while True:
        out = process.stdout.read(1)
        if len(out) == 0 and process.poll() != None:
            break
        if len(out) != 0:
            #sys.stdout.write("[unity process console ]: %s" % out)
            sys.stdout.flush()
    
    time.sleep(1)
    log.logger.info("unity batchmode build finish")
    t.stop()
    tt.stop()

def full_path(path):
    return os.path.abspath(os.path.expanduser(path))
