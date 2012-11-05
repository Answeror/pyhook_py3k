# Python3 fork of pyHook

## Introduction

Copy from [official site](http://sourceforge.net/apps/mediawiki/pyhook/index.php?title=Main_Page):

> pyHook is a python wrapper for global input hooks in Windows. Specifically it wraps the Windows SetWindowsHookEx API function using low-level keyboard (WH_KEYBOARD_LL) and mouse (WH_MOUSE_LL) hooks.
> The pyHook package provides callbacks for global mouse and keyboard events in Windows. Python applications register can event handlers for user input events such as left mouse down, left mouse up, key down, etc. and set the keyboard and/or mouse hook. The underlying C library reports information like the time of the event, the name of the window in which the event occurred, the value of the event, any keyboard modifiers, etc. Events can be logged and/or filtered.

## Install

### Build with MSVC9

Make sure you are under "Visual Studio 2008 Command Prompt".

```
python setup.py build_ext --swig=path-to-swig.exe
pip install .
```

## About this fork

### Unicode

Fixed unicode decoding bug of window title. This bug may cause crashing on exit randomly. Usually with console output:

> TypeError: MouseSwitch() takes exactly 9 arguments (1 given)

or

> TypeError: KeyboardSwitch() takes exactly 9 arguments (1 given)

### Freezing

Original pyHook will cause "cannot find \_cpyHook module" error when using PyInstaller or cx-freeze to freeze python app. You need manually rename `pyHook._cpyHook` to `_cpyHook`. Now it's compatible with cx-freeze.
