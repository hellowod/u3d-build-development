# -*- coding: utf-8 -*-

import os

import conf.argv
import conf.conf
import conf.const

def __time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_packet_name(target, istimestamp = False):
    suffix = ""
    if str(target).lower() == conf.const.buildtarget_android:
        suffix = "apk"
    if str(target).lower() == conf.const.buildtarget_ios:
        suffix = "ipa"
    if str(target).lower() == conf.const.buildtarget_standalonewindows or str(target).lower() == conf.const.buildtarget_standalonewindows64:
        suffix = "exe"
    if str(target).lower() == conf.const.buildtarget_standaloneosxintel or str(target).lower() == conf.const.buildtarget_standaloneosxintel64:
        suffix = "app"

    target_name = get_target_name(target)
    packget_name = target_name
    if istimestamp:
        packget_name = "%s_%s" % (target_name, __time())

    return "%s/%s.%s" % (target_name, packget_name, suffix)

def get_target_name(target):
    return str(target).lower()

def get_publist_packet_name(target):
    packet_name = ""
    if str(target).lower() == conf.const.buildtarget_android:
        packet_name = "unity-android.apk"
    if str(target).lower() == conf.const.buildtarget_ios:
        packet_name = "unity-iphone.ipa"
    if str(target).lower() == conf.const.buildtarget_standalonewindows:
        packet_name = "unity-window.exe"
    if str(target).lower() == conf.const.buildtarget_standalonewindows64:
        packet_name = "unity-window64.exe"
    if str(target).lower() == conf.const.buildtarget_standaloneosxintel:
        packet_name = "unity-osxintel.app"
    if str(target).lower() == conf.const.buildtarget_standaloneosxintel64:
        packet_name = "unity-osxintel64.exe"
    return packet_name

def get_project_name():
    return "sanguo2"
