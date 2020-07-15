# -*- coding: utf-8 -*-

import os

import conf.conf
import conf.argv
import conf.const
import log.logger
import yelp.path

def before_handler():
    pass

def after_handler():
    if conf.argv.get_buildtype() == conf.const.buildtarget_ios:
        _xcodebuild_clean = xcodebuild_clean()
        log.logger.info("step ===1=== %s" % _xcodebuild_clean)
        os.system(_xcodebuild_clean)

        _xcodebuild_archive = xcodebuild_archive()
        log.logger.info("step ===2=== %s" % _xcodebuild_archive)
        os.system(_xcodebuild_archive)

        _xcodebuild_exportarchive = xcodebuild_exportarchive()
        log.logger.info("step ===3=== %s" % _xcodebuild_exportarchive)
        os.system(_xcodebuild_exportarchive)
    else:
        log.logger.info("android window osxintel platform not process step 1, 2, 3.")

    if conf.argv.get_runnertype() != conf.const.runnertype_assetbundle:
        _cp_archive_packet = cp_archive_packet()
        log.logger.info("step ===4=== %s" % _cp_archive_packet)
        if len(_cp_archive_packet) > 0:
            os.system(_cp_archive_packet)

    _scp_archive_packet = scp_archive_packet()
    if _scp_archive_packet != None:
        log.logger.info("step ===5=== %s" % str(_scp_archive_packet).replace(_scp_archive_packet, "****"))
        os.system("export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/usr/local/git/bin")
        os.system(_scp_archive_packet)

def cp_archive_packet():
    if conf.argv.get_buildtype() == conf.const.buildtarget_ios:
        return "cp -R %s/Unity-iPhone.ipa %s" % (get_archive_path(), get_publist_path())
    else:
        return "cp -R %s %s" % (get_archive_path(), get_publist_path())
    
def scp_archive_packet():
    base_name = "%s/%s" % (conf.conf.get_io_inhouseftp(), yelp.path.get_project_name())
    if str(conf.argv.get_buildtype()).lower() == conf.const.buildtarget_android:
        return "/usr/bin/scp %s %s" % (get_publist_path(), base_name + ".apk")
    elif str(conf.argv.get_buildtype()).lower() == conf.const.buildtarget_ios:
        return "/usr/bin/scp %s %s" % (get_publist_path(), base_name + ".ipa")
    else:
        log.logger.info("inhouse not support other platform.")
    return None

def xcodebuild_clean():
    return "cd %s && \
            xcodebuild clean" % (get_archive_path())

def xcodebuild_archive():
    return "cd %s && \
            xcodebuild archive \
				-workspace %s \
                -scheme Unity-iPhone \
                -configuration %s \
                -archivePath Unity-iPhone.xcarchive \
                CODE_SIGN_IDENTITY=%s \
                PROVISIONING_PROFILE=%s" % (get_archive_path(), get_workspace(), get_configuration(), conf.conf.get_ios_p12(), conf.conf.get_ios_mobileprovision())

def xcodebuild_exportarchive():
    return "cd %s && \
            xcodebuild -exportArchive \
                -archivePath Unity-iPhone.xcarchive \
                -exportPath ./ \
                -exportOptionsPlist %s \
                CODE_SIGN_IDENTITY=%s \
                PROVISIONING_PROFILE=%s" % (get_archive_path(), conf.conf.get_ios_plist(), conf.conf.get_ios_p12(), conf.conf.get_ios_mobileprovision())

def get_archive_path():
    return conf.conf.get_io_archive_all(yelp.path.get_packet_name(conf.argv.get_buildtype()))
	
def get_workspace():
	return ""
	
def get_configuration():
	return "Debug"

def get_publist_path():
    return conf.conf.get_io_publish_all(yelp.path.get_publist_packet_name(conf.argv.get_buildtype()))