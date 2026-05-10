[app]
title = TermuxApp
package.name = termuxapk
package.domain = org.alamin
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.arch = arm64-v8a
android.api = 31
android.minapi = 21
android.ndk = 23b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
