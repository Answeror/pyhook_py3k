import os, os.path, sys, shutil
from distutils.sysconfig import get_python_inc
from distutils.core import setup, Extension
from distutils.command.build_ext import build_ext

libs = ['user32']

setup(name="pyHook", version="1.1",
      author="Peter Parente",
      author_email="parente@cs.unc.edu",
      url="http://www.cs.unc.edu/Research/assist/",
      description="pyHook: Python wrapper for out-of-context input hooks in Windows",
      packages = ['pyHook'],
      ext_modules = [Extension('pyHook._cpyHook', ['pyHook/cpyHook.i'], libraries=libs)],
      data_files=[('Lib/site-packages/pyHook', ["pyHook/LICENSE.txt"])]
      )