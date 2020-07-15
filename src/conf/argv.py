# -*- coding: utf-8 -*-

import sys
import getopt

import log.logger

USAGE = """
require version : python 3.6.3

usage: python main.py -p platform -c configure

options: short
    -h List available subcommands and some concept guides
    -b Specify a to build target, such as Android iOS StandaloneWindows 
       StandaloneWindows64 StandaloneOSXIntel or StandaloneOSXIntel64
    -r Specify the runner type, such as application or assetbundle etc
    -c Specify the build configurations, such as development inhouse or distribution
    -i Whether to close the compile command il2cpp

options: long
    --help List available subcommands and some concept guides
    
    --buildtype Specify a platform to build, such as Android iOS StandaloneWindows 
       StandaloneWindows64 StandaloneOSXIntel or StandaloneOSXIntel64
    --runnertype Specify the build type, such as application or assetbundle etc
    --configure Specify the build configurations, such as debug or release
	--il2cpp Whether to close the compile command il2cpp

config: build.conf
    Specify the configuration information construction of information,
    such as project path, engine path, input and output path etc

example:
    username> python main.py -b Android -r all -c debug -e path1 -a path2 -s pathsdk -noil2cpp
    username> python main.py -b Android -r application -c debug -e path1 -a path2 -s pathsdk -noil2cpp
    username> python main.py -b Android -r assetbundle -c debug -e path1 -a path2 -s pathsdk -noil2cpp

shell example:
   username> build.bat -r all -b android -c inhouse

'python main.py -h' or 'python main.py --help' to see help
"""

ARGV_COUNT = 3

def parse_argv(args):
    global buildtype
    global runnertype
    global configure
    global il2cpp

    try:
        opts, _ = getopt.getopt(args[1:],
        "hb:r:c:i:",
         ["help", "buildtype=", "runnertype=", "configure=", "il2cpp="])
    except getopt.GetoptError:
        log.logger.warn("input argv error...")
        print(USAGE)
        return False

    if len(opts) < ARGV_COUNT:
        log.logger.warn("input argv error...")
        print(USAGE)
        return False

    for key, value in opts:
        if key in ("-h", "--help"):
            print(USAGE)
            return False
        if key in ("-b", "--buildtype"):
            buildtype = value
        if key in ("-r", "--runnertype"):
            runnertype = value
        if key in ("-c", "--configure"):
            configure = value
        if key in ("-i", "--il2cpp"):
            il2cpp = value
    log.logger.info("#######argv build buildtype=%s" % get_buildtype())
    log.logger.info("#######argv build runnertype=%s" % get_runnertype())
    log.logger.info("#######argv build configure=%s" % get_configure())
    log.logger.info("#######argv build il2cpp=%s" % get_il2cpp())

    return True

def get_buildtype():
    return str.strip(str(buildtype).lower())

def get_runnertype():
    return str.strip(str(runnertype).lower())

def get_configure():
    return str.strip(str(configure).lower())

def get_il2cpp():
    return str.strip(str(il2cpp).lower())

