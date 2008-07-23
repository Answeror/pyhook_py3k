%module cpyHook
%include typemaps.i

%{
  #define _WIN32_WINNT 0x400
  #include "windows.h"
  
  // These definitions are missing from some Windows Platform SDKs, so define
  // them if yet undefined.
  #ifndef MAPVP_VK_TO_VSC
    #define MAPVK_VK_TO_VSC 0
  #endif

  #ifndef MAPVK_VSC_TO_VK
    #define MAPVK_VSC_TO_VK 1
  #endif

  #ifndef MAPVK_VK_TO_CHAR
  #define MAPVK_VK_TO_CHAR 2
  #endif

  #ifndef MAPVK_VSC_TO_VK_EX
    #define MAPVK_VSC_TO_VK_EX 3
  #endif

  PyObject* callback_funcs[WH_MAX];
  HHOOK hHooks[WH_MAX];
  BYTE key_state[256];
%}

%typemap(python, in) PyObject *pyfunc {
  if (!PyCallable_Check($input)) {
    PyErr_SetString(PyExc_TypeError, "Need a callable object");
    return NULL;
  }
  $1 = $input;
}

%init %{
  memset(key_state, 0, 256);
  memset(callback_funcs, 0, WH_MAX);
  memset(hHooks, 0, WH_MAX);
  PyEval_InitThreads();
  
  // get initial key state
  Py_BEGIN_ALLOW_THREADS
	key_state[VK_NUMLOCK] = (GetKeyState(VK_NUMLOCK)&0x0001) ? 0x01 : 0x00;
	key_state[VK_CAPITAL] = (GetKeyState(VK_CAPITAL)&0x0001) ? 0x01 : 0x00;
	key_state[VK_SCROLL] = (GetKeyState(VK_SCROLL)&0x0001) ? 0x01 : 0x00;
	Py_END_ALLOW_THREADS
%}

%wrapper %{
  unsigned short ConvertToASCII(unsigned int keycode, unsigned int scancode);
	void UpdateKeyState(unsigned int vkey, int msg);

  LRESULT CALLBACK cLLKeyboardCallback(int code, WPARAM wParam, LPARAM lParam) {
    PyObject *arglist, *r;
    PKBDLLHOOKSTRUCT kbd;
    HWND hwnd;
    PSTR win_name = NULL;
    unsigned short ascii = 0;
    static int win_len;
    static long result;
    long pass = 1;
    PyGILState_STATE gil;

    // if message code < 0, return immediately
    if(code<0)
        CallNextHookEx(hHooks[WH_KEYBOARD_LL], code, wParam, lParam);

    // get the GIL
    gil = PyGILState_Ensure();

    // cast to a keyboard event struct
    kbd = (PKBDLLHOOKSTRUCT)lParam;
    // get the current foreground window (might not be the real window that received the event)
    hwnd = GetForegroundWindow();

    // grab the window name if possible
    win_len = GetWindowTextLength(hwnd);
    if(win_len > 0) {
      win_name = (PSTR) malloc(sizeof(char) * win_len + 1);
      GetWindowText(hwnd, win_name, win_len + 1);
    }

    // convert to an ASCII code if possible
    ascii = ConvertToASCII(kbd->vkCode, kbd->scanCode);

    // pass the message on to the Python function
    arglist = Py_BuildValue("(iiiiiiiz)", wParam, kbd->vkCode, kbd->scanCode, ascii,
                            kbd->flags, kbd->time, hwnd, win_name);
    r = PyObject_CallObject(callback_funcs[WH_KEYBOARD_LL], arglist);

    // check if we should pass the event on or not
    if(r == NULL)
      PyErr_Print();
    else
      pass = PyInt_AsLong(r);

    Py_XDECREF(r);
    Py_DECREF(arglist);
    // release the GIL
    PyGILState_Release(gil);

    // free the memory for the window name
    if(win_name != NULL)
      free(win_name);

    // decide whether or not to call the next hook
    if(code < 0 || pass) {
			UpdateKeyState(kbd->vkCode, wParam);
      result = CallNextHookEx(hHooks[WH_KEYBOARD_LL], code, wParam, lParam);
    } else {
    	// return a non-zero to prevent further processing
      result = 42;
		}
    return result;
  }

  LRESULT CALLBACK cLLMouseCallback(int code, WPARAM wParam, LPARAM lParam) {
    PyObject *arglist, *r;
    PMSLLHOOKSTRUCT ms;
    HWND hwnd;
    PSTR win_name = NULL;
    static int win_len;
    static long result;
    long pass = 1;
    PyGILState_STATE gil;

    // get the GIL
    gil = PyGILState_Ensure();

    //pass the message on to the Python function
    ms = (PMSLLHOOKSTRUCT)lParam;
    hwnd = WindowFromPoint(ms->pt);

    //grab the window name if possible
    win_len = GetWindowTextLength(hwnd);
    if(win_len > 0) {
      win_name = (PSTR) malloc(sizeof(char) * win_len + 1);
      GetWindowText(hwnd, win_name, win_len + 1);
    }

    //build the argument list to the callback function
    arglist = Py_BuildValue("(iiiiiiiz)", wParam, ms->pt.x, ms->pt.y, ms->mouseData,
                            ms->flags, ms->time, hwnd, win_name);
    r = PyObject_CallObject(callback_funcs[WH_MOUSE_LL], arglist);

    // check if we should pass the event on or not
    if(r == NULL)
      PyErr_Print();
    else
      pass = PyInt_AsLong(r);

    Py_XDECREF(r);
    Py_DECREF(arglist);
    // release the GIL
    PyGILState_Release(gil);

    //free the memory for the window name
    if(win_name != NULL)
      free(win_name);

    // decide whether or not to call the next hook
    if(code < 0 || pass)
      result = CallNextHookEx(hHooks[WH_MOUSE_LL], code, wParam, lParam);
    else {
    	// return non-zero to prevent further processing
      result = 42;
    }
    return result;
  }

  int cSetHook(int idHook, PyObject *pyfunc) {
    HINSTANCE hMod;

    //make sure we have a valid hook number
    if(idHook > WH_MAX || idHook < WH_MIN) {
      PyErr_SetString(PyExc_ValueError, "Hooking error: invalid hook ID");
    }

    //get the module handle
    Py_BEGIN_ALLOW_THREADS
    // try to get handle for current file - will succeed if called from a compiled .exe
    hMod = GetModuleHandle(NULL);
    if(NULL == hMod)    // otherwise use name for DLL
        hMod = GetModuleHandle("_cpyHook.pyd");
    Py_END_ALLOW_THREADS

    //switch on the type of hook so we point to the right C callback
    switch(idHook) {
      case WH_MOUSE_LL:
        if(callback_funcs[idHook] != NULL)
          break;

        callback_funcs[idHook] = pyfunc;
        Py_INCREF(callback_funcs[idHook]);

        Py_BEGIN_ALLOW_THREADS
        hHooks[idHook] = SetWindowsHookEx(WH_MOUSE_LL, cLLMouseCallback, (HINSTANCE) hMod, 0);
        Py_END_ALLOW_THREADS
        break;

      case WH_KEYBOARD_LL:
        if(callback_funcs[idHook] != NULL)
          break;

        callback_funcs[idHook] = pyfunc;
        Py_INCREF(callback_funcs[idHook]);

        Py_BEGIN_ALLOW_THREADS
        hHooks[idHook] = SetWindowsHookEx(WH_KEYBOARD_LL, cLLKeyboardCallback, (HINSTANCE) hMod, 0);
        Py_END_ALLOW_THREADS
        break;

      default:
       return 0;
    }

    if(!hHooks[idHook]) {
      PyErr_SetString(PyExc_TypeError, "Could not set hook");
    }

    return 1;
  }

  int cUnhook(int idHook) {
    BOOL result;

    //make sure we have a valid hook number
    if(idHook > WH_MAX || idHook < WH_MIN) {
      PyErr_SetString(PyExc_ValueError, "Invalid hook ID");
    }

    //unhook the callback
    Py_BEGIN_ALLOW_THREADS
    result = UnhookWindowsHookEx(hHooks[idHook]);
    Py_END_ALLOW_THREADS

    if(result) {
      //decrease the ref to the Python callback
    	Py_DECREF(callback_funcs[idHook]);
      callback_funcs[idHook] = NULL;
    }

    return result;
  }
  
  void SetKeyState(unsigned int vkey, int down) {
	  // (1 > 0) ? True : False
 		if (vkey == VK_MENU || vkey == VK_LMENU || vkey == VK_RMENU) {
 			key_state[vkey] = (down) ? 0x80 : 0x00;
 			key_state[VK_MENU] = key_state[VK_LMENU] | key_state[VK_RMENU];
 		} else if (vkey == VK_SHIFT || vkey == VK_LSHIFT || vkey == VK_RSHIFT) {
 			key_state[vkey] = (down) ? 0x80 : 0x00;
 			key_state[VK_SHIFT] = key_state[VK_LSHIFT] | key_state[VK_RSHIFT];
 		} else if (vkey == VK_CONTROL || vkey == VK_LCONTROL || vkey == VK_RCONTROL) {
 			key_state[vkey] = (down) ? 0x80 : 0x00;
 			key_state[VK_CONTROL] = key_state[VK_LCONTROL] | key_state[VK_RCONTROL];
 		} else if (vkey == VK_NUMLOCK && !down) {
 			key_state[VK_NUMLOCK] = !key_state[VK_NUMLOCK];
 		} else if (vkey == VK_CAPITAL && !down) {
 			key_state[VK_CAPITAL] = !key_state[VK_CAPITAL];
 		} else if (vkey == VK_SCROLL && !down) {
 			key_state[VK_SCROLL] = !key_state[VK_SCROLL];
 		}
  }
  
  void UpdateKeyState(unsigned int vkey, int msg) {
  	if (msg == WM_KEYDOWN || msg == WM_SYSKEYDOWN) {
			SetKeyState(vkey, 1);
  	} else if (msg == WM_KEYUP || msg == WM_SYSKEYUP) {
			SetKeyState(vkey, 0);
  	}
  }
  
  unsigned int cGetKeyState(unsigned int vkey) {
  	return key_state[vkey];
  }

  unsigned short ConvertToASCII(unsigned int keycode, unsigned int scancode) {
    unsigned short c;

    Py_BEGIN_ALLOW_THREADS
    c = MapVirtualKey(keycode, MAPVK_VK_TO_CHAR);
    Py_END_ALLOW_THREADS
    return c;
  }
%}

unsigned int cGetKeyState(unsigned int vkey);
int cSetHook(int idHook, PyObject *pyfunc);
int cUnhook(int idHook);
