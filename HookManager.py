from pyHook.cpyHook import *

class HookConstants:
  WH_MIN = -1
  WH_MSGFILTER = -1
  WH_JOURNALRECORD = 0
  WH_JOURNALPLAYBACK = 1
  WH_KEYBOARD = 2
  WH_GETMESSAGE = 3
  WH_CALLWNDPROC = 4
  WH_CBT = 5
  WH_SYSMSGFILTER = 6
  WH_MOUSE = 7
  WH_HARDWARE = 8
  WH_DEBUG = 9
  WH_SHELL = 10
  WH_FOREGROUNDIDLE = 11
  WH_CALLWNDPROCRET = 12
  WH_KEYBOARD_LL = 13
  WH_MOUSE_LL = 14
  WH_MAX = 15

  WM_MOUSEFIRST = 0x0200
  WM_MOUSEMOVE = 0x0200
  WM_LBUTTONDOWN = 0x0201
  WM_LBUTTONUP = 0x0202
  WM_LBUTTONDBLCLK = 0x0203
  WM_RBUTTONDOWN =0x0204
  WM_RBUTTONUP = 0x0205
  WM_RBUTTONDBLCLK = 0x0206
  WM_MBUTTONDOWN = 0x0207
  WM_MBUTTONUP = 0x0208
  WM_MBUTTONDBLCLK = 0x0209
  WM_MOUSEWHEEL = 0x020A
  WM_MOUSELAST = 0x020A

  WM_KEYFIRST = 0x0100
  WM_KEYDOWN = 0x0100
  WM_KEYUP = 0x0101
  WM_CHAR = 0x0102
  WM_DEADCHAR = 0x0103
  WM_SYSKEYDOWN = 0x0104
  WM_SYSKEYUP = 0x0105
  WM_SYSCHAR = 0x0106
  WM_SYSDEADCHAR = 0x0107
  WM_KEYLAST = 0x0108


  #VK_0 thru VK_9 are the same as ASCII '0' thru '9' (0x30 -' : 0x39)
  #VK_A thru VK_Z are the same as ASCII 'A' thru 'Z' (0x41 -' : 0x5A)

  #virtual keycode constant names to virtual keycodes numerical id
  vk_to_id = {'VK_LBUTTON' : 0x01, 'VK_RBUTTON' : 0x02, 'VK_CANCEL' : 0x03, 'VK_MBUTTON' : 0x04,
  'VK_BACK' : 0x08, 'VK_TAB' : 0x09, 'VK_CLEAR' : 0x0C, 'VK_RETURN' : 0x0D, 'VK_SHIFT' : 0x10,
  'VK_CONTROL' : 0x11, 'VK_MENU' : 0x12, 'VK_PAUSE' : 0x13, 'VK_CAPITAL' : 0x14, 'VK_KANA' : 0x15,
  'VK_HANGEUL' : 0x15, 'VK_HANGUL' : 0x15, 'VK_JUNJA' : 0x17, 'VK_FINAL' : 0x18, 'VK_HANJA' : 0x19,
  'VK_KANJI' : 0x19, 'VK_ESCAPE' : 0x1B, 'VK_CONVERT' : 0x1C, 'VK_NONCONVERT' : 0x1D, 'VK_ACCEPT' : 0x1E,
  'VK_MODECHANGE' : 0x1F, 'VK_SPACE' : 0x20, 'VK_PRIOR' : 0x21, 'VK_NEXT' : 0x22, 'VK_END' : 0x23,
  'VK_HOME' : 0x24, 'VK_LEFT' : 0x25, 'VK_UP' : 0x26, 'VK_RIGHT' : 0x27, 'VK_DOWN' : 0x28,
  'VK_SELECT' : 0x29, 'VK_PRINT' : 0x2A, 'VK_EXECUTE' : 0x2B, 'VK_SNAPSHOT' : 0x2C, 'VK_INSERT' : 0x2D,
  'VK_DELETE' : 0x2E, 'VK_HELP' : 0x2F, 'VK_LWIN' : 0x5B, 'VK_RWIN' : 0x5C, 'VK_APPS' : 0x5D,
  'VK_NUMPAD0' : 0x60, 'VK_NUMPAD1' : 0x61, 'VK_NUMPAD2' : 0x62, 'VK_NUMPAD3' : 0x63, 'VK_NUMPAD4' : 0x64,
  'VK_NUMPAD5' : 0x65, 'VK_NUMPAD6' : 0x66, 'VK_NUMPAD7' : 0x67, 'VK_NUMPAD8' : 0x68, 'VK_NUMPAD9' : 0x69,
  'VK_MULTIPLY' : 0x6A, 'VK_ADD' : 0x6B, 'VK_SEPARATOR' : 0x6C, 'VK_SUBTRACT' : 0x6D, 'VK_DECIMAL' : 0x6E,
  'VK_DIVIDE' : 0x6F ,'VK_F1' : 0x70, 'VK_F2' : 0x71, 'VK_F3' : 0x72, 'VK_F4' : 0x73, 'VK_F5' : 0x74,
  'VK_F6' : 0x75, 'VK_F7' : 0x76, 'VK_F8' : 0x77, 'VK_F9' : 0x78, 'VK_F10' : 0x79, 'VK_F11' : 0x7A,
  'VK_F12' : 0x7B, 'VK_F13' : 0x7C, 'VK_F14' : 0x7D, 'VK_F15' : 0x7E, 'VK_F16' : 0x7F, 'VK_F17' : 0x80,
  'VK_F18' : 0x81, 'VK_F19' : 0x82, 'VK_F20' : 0x83, 'VK_F21' : 0x84, 'VK_F22' : 0x85, 'VK_F23' : 0x86,
  'VK_F24' : 0x87, 'VK_NUMLOCK' : 0x90, 'VK_SCROLL' : 0x91, 'VK_LSHIFT' : 0xA0, 'VK_RSHIFT' : 0xA1,
  'VK_LCONTROL' : 0xA2, 'VK_RCONTROL' : 0xA3, 'VK_LMENU' : 0xA4, 'VK_RMENU' : 0xA5, 'VK_PROCESSKEY' : 0xE5,
  'VK_ATTN' : 0xF6, 'VK_CRSEL' : 0xF7, 'VK_EXSEL' : 0xF8, 'VK_EREOF' : 0xF9, 'VK_PLAY' : 0xFA,
  'VK_ZOOM' : 0xFB, 'VK_NONAME' : 0xFC, 'VK_PA1' : 0xFD, 'VK_OEM_CLEAR' : 0xFE, 'VK_BROWSER_BACK' : 0xA6,
  'VK_BROWSER_FORWARD' : 0xA7, 'VK_BROWSER_REFRESH' : 0xA8, 'VK_BROWSER_STOP' : 0xA9, 'VK_BROWSER_SEARCH' : 0xAA,
  'VK_BROWSER_FAVORITES' : 0xAB, 'VK_BROWSER_HOME' : 0xAC, 'VK_VOLUME_MUTE' : 0xAD, 'VK_VOLUME_DOWN' : 0xAE,
  'VK_VOLUME_UP' : 0xAF, 'VK_MEDIA_NEXT_TRACK' : 0xB0, 'VK_MEDIA_PREV_TRACK' : 0xB1, 'VK_MEDIA_STOP' : 0xB2,
  'VK_MEDIA_PLAY_PAUSE' : 0xB3, 'VK_LAUNCH_MAIL' : 0xB4, 'VK_LAUNCH_MEDIA_SELECT' : 0xB5, 'VK_LAUNCH_APP1' : 0xB6,
  'VK_LAUNCH_APP2' : 0xB7, 'VK_OEM_1' : 0xBA, 'VK_OEM_PLUS' : 0xBB, 'VK_OEM_COMMA' : 0xBC, 'VK_OEM_MINUS' : 0xBD,
  'VK_OEM_PERIOD' : 0xBE, 'VK_OEM_2' : 0xBF, 'VK_OEM_3' : 0xC0, 'VK_OEM_4' : 0xDB, 'VK_OEM_5' : 0xDC,
  'VK_OEM_6' : 0xDD, 'VK_OEM_7' : 0xDE, 'VK_OEM_8' : 0xDF, 'VK_OEM_102' : 0xE2, 'VK_PROCESSKEY' : 0xE5,
  'VK_PACKET' : 0xE7}

  #inverse mapping of keycodes
  id_to_vk = dict([(v,k) for k,v in vk_to_id.items()])

  #message constants to message names
  msg_to_name = {WM_MOUSEMOVE : 'mouse move', WM_LBUTTONDOWN : 'mouse left down',
                 WM_LBUTTONUP : 'mouse left up', WM_LBUTTONDBLCLK : 'mouse left double',
                 WM_RBUTTONDOWN : 'mouse right down', WM_RBUTTONUP : 'mouse right up',
                 WM_RBUTTONDBLCLK : 'mouse right double',  WM_MBUTTONDOWN : 'mouse middle down',
                 WM_MBUTTONUP : 'mouse middle up', WM_MBUTTONDBLCLK : 'mouse middle double',
                 WM_MOUSEWHEEL : 'mouse wheel',  WM_KEYDOWN : 'key down',
                 WM_KEYUP : 'key up', WM_CHAR : 'key char', WM_DEADCHAR : 'key dead char',
                 WM_SYSKEYDOWN : 'key sys down', WM_SYSKEYUP : 'key sys up',
                 WM_SYSCHAR : 'key sys char', WM_SYSDEADCHAR : 'key sys dead char'}

  def MsgToName(cls, msg):
    return HookConstants.msg_to_name.get(msg)

  def VKeyToID(cls, vkey):
    return HookConstants.vk_to_id.get(vkey)

  def IDToName(cls, code):
    text = None
    if (code >= 0x30 and code <= 0x39) or (code >= 0x41 and code <= 0x5A):
      text = chr(code)
    else:
      text = HookConstants.id_to_vk.get(code)
      if text is not None:
        text = text[3:].title()

    return text

  MsgToName=classmethod(MsgToName)
  IDToName=classmethod(IDToName)
  VKeyToID=classmethod(VKeyToID)

class HookEvent(object):
  def __init__(self, msg, time, hwnd, window_name):
    self.msg = msg
    self.time = time
    self.hwnd = hwnd
    self.window_name = window_name

  def GetMessageName(self):
    return HookConstants.MsgToName(self.msg)
  def GetMessage(self):
    return self.msg
  def GetTime(self):
    return self.time
  def GetWindow(self):
    return self.hwnd
  def GetWindowName(self):
    return self.window_name

  MessageName = property(fget=GetMessageName)
  Message = property(fget=GetMessage)
  Time = property(fget=GetTime)
  Window = property(fget=GetWindow)
  WindowName = property(fget=GetWindowName)

class MouseEvent(HookEvent):
  def __init__(self, msg, x, y, data, flags, time, hwnd, window_name):
    HookEvent.__init__(self, msg, time, hwnd, window_name)
    self.pos = (x,y)

    if data > 0: w = 1
    elif data < 0: w = -1
    else: w = 0
    self.wheel = w

    self.injected = flags & 0x01

  def GetPosition(self):
    return self.pos
  def GetWheel(self):
    return self.wheel
  def IsInjected(self):
    return self.injected

  Position = property(fget=GetPosition)
  Wheel = property(fget=GetWheel)
  Injected = property(fget=IsInjected)

class KeyboardEvent(HookEvent):
  def __init__(self, msg, vk_code, scan_code, flags, time, hwnd, window_name):
    HookEvent.__init__(self, msg, time, hwnd, window_name)

    self.vk_code = vk_code
    self.scan_code = scan_code
    self.flags = flags

  def GetCharacter(self):
    return GetAsciiCharacter(self.vk_code, self.scan_code)
  def GetKey(self):
    return HookConstants.IDToName(self.vk_code)
  def GetKeyID(self):
    return self.vk_code
  def GetScanCode(self):
    return self.scan_code
  def IsExtended(self):
    return self.flags & 0x01
  def IsInjected(self):
    return self.flags & 0x10
  def IsAlt(self):
    return self.flags & 0x20
  def IsTransition(self):
    return self.flags & 0x80

  Key = property(fget=GetKey)
  KeyID = property(fget=GetKeyID)
  ScanCode = property(fget=GetScanCode)
  Extended = property(fget=IsExtended)
  Injected = property(fget=IsInjected)
  Alt = property(fget=IsAlt)
  Transition = property(fget=IsTransition)
  Char = property(fget=GetCharacter)

class HookManager(object):
  def __init__(self):
    '''Initialize an instance by setting up an empty switch network.'''
    self.mouse_funcs = {}
    self.keyboard_funcs = {}

    self.mouse_hook = False
    self.key_hook = False

  def __del__(self):
    '''Unhook all registered hooks.'''
    self.UnhookMouse()
    self.UnhookKeyboard()

  def HookMouse(self):
    '''Begin watching for mouse events.'''
    cSetHook(HookConstants.WH_MOUSE_LL, self.MouseSwitch)
    self.mouse_hook = True

  def HookKeyboard(self):
    '''Begin watching for keyboard events.'''
    cSetHook(HookConstants.WH_KEYBOARD_LL, self.KeyboardSwitch)
    self.keyboard_hook = True

  def UnhookMouse(self):
    '''End watching for mouse events.'''
    if self.mouse_hook:
      cUnhook(HookConstants.WH_MOUSE_LL)
      self.mouse_hook = False

  def UnhookKeyboard(self):
    '''End watching for keyboard events.'''
    if self.keyboard_hook:
      cUnhook(HookConstants.WH_KEYBOARD_LL)
      self.keyboard_hook = False

  def MouseSwitch(self, msg, x, y, data, flags, time, hwnd, window_name):
    '''Pass a mouse event on to the appropriate handler if one is registered.

    Params:

    'msg': The integer ID of the Windows message

    'x': The x coordinate of the mouse event

    'y': The y coordinate of the mouse event

    'data': The data associated with the mouse event (scroll information)

    'flags': Flags associated with the mouse event (injected or not)

    'time': The time since the epoch of the mouse event

    'hwnd': Handle to the window that will receive the event
    '''
    event = MouseEvent(msg, x, y, data, flags, time, hwnd, window_name)
    func = self.mouse_funcs.get(msg)
    if func:
      return func(event)
    else:
      return True

  def KeyboardSwitch(self, msg, vk_code, scan_code, flags, time, hwnd, win_name):
    '''Pass a keyboard event on to the appropriate handler if one is registered.

    Params:

    'msg': The integer ID of the Windows message

    'vk_code': The virtual keycode of the key

    'scan_code': The scan code of the key

    'flags': Flags associated with the key event (injected or not, extended key, etc.)

    'time': The time since the epoch of the key event

    'hwnd': Handle to the window that will receive the event
    '''
    event = KeyboardEvent(msg, vk_code, scan_code, flags, time, hwnd, win_name)
    func = self.keyboard_funcs.get(msg)
    if func:
      return func(event)
    else:
      return True

  def SubscribeMouseMove(self, func):
    if func is None:
      self.disconnect(self.mouse_funcs, HookConstants.WM_MOUSEMOVE)
    else:
      self.connect(self.mouse_funcs, HookConstants.WM_MOUSEMOVE, func)

  def SubscribeMouseLeftUp(self, func):
    if func is None:
      self.disconnect(self.mouse_funcs, HookConstants.WM_LBUTTONUP)
    else:
      self.connect(self.mouse_funcs, HookConstants.WM_LBUTTONUP, func)

  def SubscribeMouseLeftDown(self, func):
    if func is None:
      self.disconnect(self.mouse_funcs, HookConstants.WM_LBUTTONDOWN)
    else:
      self.connect(self.mouse_funcs, HookConstants.WM_LBUTTONDOWN, func)

  def SubscribeMouseLeftDbl(self, func):
    if func is None:
      self.disconnect(self.mouse_funcs, HookConstants.WM_LBUTTONDBLCLK)
    else:
      self.connect(self.mouse_funcs, HookConstants.WM_LBUTTONDBLCLK, func)

  def SubscribeMouseRightUp(self, func):
    if func is None:
      self.disconnect(self.mouse_funcs, HookConstants.WM_RBUTTONUP)
    else:
      self.connect(self.mouse_funcs, HookConstants.WM_RBUTTONUP, func)

  def SubscribeMouseRightDown(self, func):
    if func is None:
      self.disconnect(self.mouse_funcs, HookConstants.WM_RBUTTONDOWN)
    else:
      self.connect(self.mouse_funcs, HookConstants.WM_RBUTTONDOWN, func)

  def SubscribeMouseRightDbl(self, func):
    if func is None:
      self.disconnect(self.mouse_funcs, HookConstants.WM_RBUTTONDBLCLK)
    else:
      self.connect(self.mouse_funcs, HookConstants.WM_RBUTTONDBLCLK, func)

  def SubscribeMouseMiddleUp(self, func):
    if func is None:
      self.disconnect(self.mouse_funcs, HookConstants.WM_MBUTTONUP)
    else:
      self.connect(self.mouse_funcs, HookConstants.WM_MBUTTONUP, func)

  def SubscribeMouseMiddleDown(self, func):
    if func is None:
      self.disconnect(self.mouse_funcs, HookConstants.WM_MBUTTONDOWN)
    else:
      self.connect(self.mouse_funcs, HookConstants.WM_MBUTTONDOWN, func)

  def SubscribeMouseMiddleDbl(self, func):
    if func is None:
      self.disconnect(self.mouse_funcs, HookConstants.WM_MBUTTONDBLCLK)
    else:
      self.connect(self.mouse_funcs, HookConstants.WM_MBUTTONDBLCLK, func)

  def SubscribeMouseWheel(self, func):
    if func is None:
      self.disconnect(self.mouse_funcs, HookConstants.WM_MOUSEWHEEL)
    else:
      self.connect(self.mouse_funcs, HookConstants.WM_MOUSEWHEEL, func)

  def SubscribeMouseAll(self, func):
    self.MouseMove = func
    self.MouseWheel = func
    self.SubscribeMouseAllButtons(func)

  def SubscribeMouseAllButtons(self, func):
    self.SubscribeMouseAllButtonsDown(func)
    self. SubscribeMouseAllButtonsUp(func)
    self.SubscribeMouseAllButtonsDbl(func)

  def SubscribeMouseAllButtonsDown(self, func):
    self.SubscribeMouseLeftDown(func)
    self.SubscribeMouseRightDown(func)
    self.SubscribeMouseMiddleDown(func)

  def SubscribeMouseAllButtonsUp(self, func):
    self.SubscribeMouseLeftUp(func)
    self.SubscribeMouseRightUp(func)
    self.SubscribeMouseMiddleUp(func)

  def SubscribeMouseAllButtonsDbl(self, func):
    self.SubscribeMouseLeftDbl(func)
    self.SubscribeMouseRightDbl(func)
    self.SubscribeMouseMiddleDbl(func)

  def SubscribeKeyDown(self, func):
    if func is None:
      self.disconnect(self.keyboard_funcs, HookConstants.WM_KEYDOWN)
      self.disconnect(self.keyboard_funcs, HookConstants.WM_SYSKEYDOWN)
    else:
      self.connect(self.keyboard_funcs, HookConstants.WM_KEYDOWN, func)
      self.connect(self.keyboard_funcs, HookConstants.WM_SYSKEYDOWN, func)

  def SubscribeKeyUp(self, func):
    if func is None:
      self.disconnect(self.keyboard_funcs, HookConstants.WM_KEYUP)
      self.disconnect(self.keyboard_funcs, HookConstants.WM_SYSKEYUP)
    else:
      self.connect(self.keyboard_funcs, HookConstants.WM_KEYUP, func)
      self.connect(self.keyboard_funcs, HookConstants.WM_SYSKEYUP, func)

  def SubscribeKeyChar(self, func):
    if func is None:
      self.disconnect(self.keyboard_funcs, HookConstants.WM_CHAR)
      self.disconnect(self.keyboard_funcs, HookConstants.WM_DEADCHAR)
      self.disconnect(self.keyboard_funcs, HookConstants.WM_SYSCHAR)
      self.disconnect(self.keyboard_funcs, HookConstants.WM_SYSDEADCHAR)
    else:
      self.connect(self.keyboard_funcs, HookConstants.WM_CHAR, func)
      self.connect(self.keyboard_funcs, HookConstants.WM_DEADCHAR, func)
      self.connect(self.keyboard_funcs, HookConstants.WM_SYSCHAR, func)
      self.connect(self.keyboard_funcs, HookConstants.WM_SYSDEADCHAR, func)

  def SubscribeSysKeyDown(self, func):
    if func is None:
      self.disconnect(self.keyboard_funcs, HookConstants.WM_SYSKEYDOWN)
    else:
      self.connect(self.keyboard_funcs, HookConstants.WM_SYSKEYDOWN, func)

  def SubscribeSysKeyUp(self, func):
    if func is None:
      self.disconnect(self.keyboard_funcs, HookConstants.WM_SYSKEYUP)
    else:
      self.connect(self.keyboard_funcs, HookConstants.WM_SYSKEYUP, func)


  MouseAll = property(fset=SubscribeMouseAll)
  MouseAllButtons = property(fset=SubscribeMouseAllButtons)
  MouseAllButtonsUp = property(fset=SubscribeMouseAllButtonsUp)
  MouseAllButtonsDown = property(fset=SubscribeMouseAllButtonsDown)
  MouseAllButtonsDbl = property(fset=SubscribeMouseAllButtonsDbl)

  MouseWheel = property(fset=SubscribeMouseWheel)
  MouseMove = property(fset=SubscribeMouseMove)
  MouseLeftUp = property(fset=SubscribeMouseLeftUp)
  MouseLeftDown = property(fset=SubscribeMouseLeftDown)
  MouseLeftDbl = property(fset=SubscribeMouseLeftDbl)
  MouseRightUp = property(fset=SubscribeMouseRightUp)
  MouseRightDown = property(fset=SubscribeMouseRightDown)
  MouseRightDbl = property(fset=SubscribeMouseRightDbl)
  MouseMiddleUp = property(fset=SubscribeMouseMiddleUp)
  MouseMiddleDown = property(fset=SubscribeMouseMiddleDown)
  MouseMiddleDbl = property(fset=SubscribeMouseMiddleDbl)

  KeyUp = property(fset=SubscribeKeyUp)
  KeyDown = property(fset=SubscribeKeyDown)
  KeyChar = property(fset=SubscribeKeyChar)

  def connect(self, switch, id, func):
    switch[id] = func

  def disconnect(self, switch, id):
    try:
      del switch[id]
    except:
      pass