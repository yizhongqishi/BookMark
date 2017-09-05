# /usr/bin/env python
# -*- coding : utf-8 -*-
from cx_Freeze import setup, Executable
import sys
base = "Win32GUI"
executables = [
    Executable(
        script='onlyone.py',
        targetName='assisstant.exe',
        base="Win32GUI",
        icon='laosiji.ico'
    )]

setup(name='assisstant',
      version='0.1',
      description='Sample cx_Freeze script',
      executables=executables
      )