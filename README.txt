Intro
-----
This is a Python interface to the Windows API function SetWindowsHookEx. The library currently
supports the low level keyboard and mouse hooks (since they are out-of-context callbacks).

10/11/04
- Added support for translating virtual keycodes to ASCII characters when possible
- Added support for stopping event propagation

9/13/04
- AA example was updated to work with the wx namespace
- Added support for allowing/disallowing event propagation (see example.py)
- Added a proper __init__.py to the package

Examples
--------
See the example.py file for a simple example of how to use pyHook.
See the aa hook.py file for a example of how pyHook can be used alongside our pyAA library.

Both examples require wxPython, but only because I didn't want to write my own Windows message pump.