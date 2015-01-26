#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

import re
from setuptools import setup

NAME = 'Manami'
ICON = 'app.icns'
VERSION = '1.0.0'
INFO = 'Manami - Simple Game Skeleton for Python/SDL2'
COPYRIGHT = '© 2015 CreepyPanda Software'
IDENTIFIER = 'com.creepypanda.games'

PLIST = {'CFBundleName': NAME,
         'CFBundleIconFile': ICON,
         'CFBundleVersion': VERSION,
         'CFBundleExecutable': NAME,
         'CFBundleGetInfoString': INFO,
         'CFBundleShortVersionString': re.search(r'\d\.\d', VERSION).group(0),
         'NSHumanReadableCopyright': COPYRIGHT,
         'CFBundleIdentifier': IDENTIFIER,
         'CFBundleDocumentTypes': [],
         'CFBundleURLTypes': [],
         'LSBackgroundOnly': False,
         'LSUIElement': False,
         'NSServices': []}

APP = ['manami.py']

DATA_FILES = [('', [ICON]),
              ('', ['gfx',
                    'sfx'])]

INCLUDES = ['sdl2',
            'sdl2.ext',
            'sdl2.sdlimage',
            'sdl2.sdlmixer']

FRAMEWORKS = ['/Library/Frameworks/SDL2.framework',
              '/Library/Frameworks/SDL2_image.framework',
              '/Library/Frameworks/SDL2_mixer.framework']

OPTIONS = {'argv_emulation': True,
           'frameworks': FRAMEWORKS,
           'includes': INCLUDES,
           'plist': PLIST}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)
