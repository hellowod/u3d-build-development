# -*- coding: utf-8 -*-

COMMENT = """
 ##############################################
##                                            ##
##                  v 0.9                     ##
##  <http://www.changyou.com/index.shtml>     ##
##       <xiangjinbao@cyou-inc.com>           ##
##                                            ##
##     a cross-platform build script for      ##
##     Unity3D console mode build script      ##
##                                            ##
##                                            ##
 ##############################################
"""

SPLITLINE = "###########################################################################################"

import sys
import time

import conf.argv
import conf.conf

#import core.filter

import log.logger

def sleep_time(c = 6):
    count = c
    while True:
        print(SPLITLINE)
        time.sleep(0.2)
        count = count - 1
        if count < 0:
            break

if "__main__" == __name__ :
    print(COMMENT)

    if not conf.argv.parse_argv(sys.argv):
        log.logger.info("please repeat input build params.")
        exit()
    
    try:
        core.filter.do_handler()
    except Exception as message:
        log.logger.error("build exception %s." % message)
        exit(1)