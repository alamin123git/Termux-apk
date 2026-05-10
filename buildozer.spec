[app]
title = MyTermuxApp
package.name = termuxapk
package.domain = org.alamin
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.arch = arm64-v8a
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.skip_update = False
android.accept_sdk_license = True
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
