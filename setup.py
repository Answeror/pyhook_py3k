import os, os.path, sys, shutil
from distutils.sysconfig import get_python_inc
from distutils.core import setup, Extension
from distutils.command.build_ext import build_ext

libs = ['user32']

setup(name="pyHook", version="1.0",
      py_modules = ['pyHook', 'pyHookManager'],
      ext_modules = [Extension('_pyHook',
                               ['pyHook.i'],
                               libraries=libs,
                               extra_link_args=['/SECTION:.GLOBALS,RWS']
                               )
                     ],
      )