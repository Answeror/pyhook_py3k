%module cpyHook
%include typemaps.i

%{
  #define _WIN32_WINNT 0x400
  #include "windows.h"

  PyObject* callback_funcs[WH_MAX];
  HHOOK hHooks[WH_MAX];
%}

%typemap(python, in) PyObject *pyfunc {
  if (!PyCallable_Check($input)) {
    PyErr_SetString(PyExc_TypeError, "Need a callable object");
    return NULL;
  }
  $1 = $input;
}

%init %{
  //set the arrays to NULL
  for(i=0; i < WH_MAX; i++) {
    callback_funcs[i] = NULL;
    hHooks[i] = NULL;
  }
%}

%wrapper %{
  LRESULT CALLBACK cLLKeyboardCallback(int code, WPARAM wParam, LPARAM lParam) {
    PyObject *arglist, *r;
    PKBDLLHOOKSTRUCT kbd;
    HWND hwnd;
    PSTR win_name = NULL;
    static int win_len;
    static long result;
    long pass = 1;
    PyGILState_STATE gil;
    
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

    // pass the message on to the Python function
    arglist = Py_BuildValue("(iiiiiiz)", wParam, kbd->vkCode, kbd->scanCode,
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
    if(code <  0 || pass)
      result = CallNextHookEx(hHooks[WH_KEYBOARD_LL], code, wParam, lParam);
    else
      result = 42;
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
    else
      result = 42;
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
      PyErr_SetString(PyExc_TypeError, "Hooking error: could not set hook");
    }

    return 1;
  }

  int cUnhook(int idHook) {
    BOOL result;

    //make sure we have a valid hook number
    if(idHook > WH_MAX || idHook < WH_MIN) {
      PyErr_SetString(PyExc_ValueError, "Hooking error: invalid hook ID");
    }

    //unhook the callback
    Py_BEGIN_ALLOW_THREADS
    result = UnhookWindowsHookEx(hHooks[idHook]);
    Py_END_ALLOW_THREADS

    if(result)
      callback_funcs[idHook] = NULL;

    //decrease the ref to the Python callback
    Py_DECREF(callback_funcs[idHook]);

    return result;
  }
%}

int cSetHook(int idHook, PyObject *pyfunc);
int cUnhook(int idHook);