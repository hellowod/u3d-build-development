# -*- coding: utf-8 -*-

import configparser
import os

CONF_PATH = "../../cfg/build.conf"

work_path = os.path.dirname(os.path.abspath(__file__))
conf_path = os.path.join(work_path, CONF_PATH)

conf = configparser.ConfigParser()
conf.read(conf_path)


def p_standard(str):
    return str.replace("\\", "/")

def get_work_path():
    return p_standard(work_path)

def get_conf_path():
    return p_standard(conf_path)


def get_project_path():
    return p_standard(os.path.join(os.path.abspath(""), conf.get("project", "path")))


def get_unity_appwin():
    return p_standard(conf.get("unity", "appwin"))
def get_unity_apposx():
    return p_standard(conf.get("unity", "apposx"))

def get_unity_log_abs():
    return p_standard(os.path.join(get_project_path(), "build_assetbundle.log"))

def get_unity_log_app():
    return p_standard(os.path.join(get_project_path(), "build_application.log"))

def get_unity_function_abs():
    return p_standard(conf.get("unity", "fun"))

def get_unity_function_app():
    return p_standard(conf.get("unity", "fun"))


def get_ios_p12():
    #return p_standard(os.path.join(os.path.abspath(""), conf.get("ios", "p12")))
    return conf.get("ios", "p12")

def get_ios_plist():
    return p_standard(os.path.join(os.path.abspath(""), conf.get("ios", "plist")))

def get_ios_mobileprovision():
    #return p_standard(os.path.join(os.path.abspath(""), conf.get("ios", "mobileprovision")))
    return conf.get("ios", "mobileprovision")


def get_android_sdkwin():
    return p_standard(conf.get("android", "sdkwin"))

def get_android_sdkosx():
    return p_standard(conf.get("android", "sdkosx"))

def get_android_jdkwin():
    return p_standard(conf.get("android", "jdkwin"))

def get_android_jdkosx():
    return p_standard(conf.get("android", "jdkosx"))

def get_android_ndkwin():
    return p_standard(conf.get("android", "ndkwin"))

def get_android_ndkosx():
    return p_standard(conf.get("android", "ndkosx"))

def get_android_keystore():
    return p_standard(conf.get("android", "keystore"))

def get_android_keystorepass():
    return conf.get("android", "keystorepass")

def get_android_keyaliasname():
    return conf.get("android", "keyaliasname")

def get_android_keyaliaspass():
    return conf.get("android", "keyaliaspass")


def get_io_export():
    return p_standard(os.path.join(os.path.abspath(""), conf.get("io", "export")))

def get_io_export_all(target):
    return p_standard(os.path.join(get_io_export(), str(target + "/" + target)))

def get_io_archive():
    return p_standard(os.path.join(os.path.abspath(""), conf.get("io", "archive")))

def get_io_archive_all(name):
    return p_standard(os.path.join(get_io_archive(), name))

def get_io_publish():
    return p_standard(os.path.join(os.path.abspath(""), conf.get("io", "publish")))

def get_io_publish_all(name):
    return p_standard(os.path.join(get_io_publish(), name))

def get_io_inhouseftp():
    return p_standard(conf.get("io", "inhouseftp"))


