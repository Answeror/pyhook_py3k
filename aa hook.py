from wxPython.wx import *
from pyHookManager import *
from pyAA import *

EVT_GET_AO_ID = wxNewId()
def EVT_GET_AO(win, func):
  win.Connect(-1, -1, EVT_GET_AO_ID, func)
  
class evtGetAO(wxPyEvent):
  def __init__(self, event, type):
    wxPyEvent.__init__(self)
    self.SetEventType(EVT_GET_AO_ID)
    self.HookEvent = event
    self.Type = type

class myFrame(wxFrame):
  def __init__(self):
    wxFrame.__init__(self, None, -1, 'My Frame')
    
    self.hm = HookManager()
    self.hm.MouseAllButtonsDown = self.OnMouseEvent
    self.hm.KeyDown = self.OnKeyboardEvent
  
    self.hm.HookMouse()
    self.hm.HookKeyboard()
    
    EVT_CLOSE(self, self.OnClose)
    EVT_GET_AO(self, self.OnGetAO)
  
  def OnGetAO(self, event):
    if event.Type == 'keyboard':
      ao = AccessibleObjectFromWindow(event.Window, OBJID_CLIENT)
    elif event.Type == 'mouse':
      ao = AccessibleObjectFromPoint(event.Position)

    print 
    print '---------------------------'
    print 'Event:'
    print ' ',event.MessageName
    print '  Window:', event.WindowName
    if event.Type == 'keyboard':
      print '  Key:',event.Key
    print
    print 'Object:'
    try:
      print '  Name:', ao.Name()
    except:
      print
    
    try:
      print '  Value:', ao.Value()
    except:
      print

    try:
      print '  Role:', ao.RoleText()
    except:
      print
    
    try:
      print '  Description:', ao.Description()
    except:
      print
    
    try:
      print '  State:', ao.StateText()
    except:
      print
      
    try:
      print '  Shortcut:', ao.KeyboardShortcut()
    except:
      print
    
  def OnMouseEvent(self, event):
    #wxPostEvent(self, evtGetAO(event, 'mouse'))
    event.Type = 'mouse'
    wxCallAfter(self.OnGetAO, event)

  def OnKeyboardEvent(self, event):
    #wxPostEvent(self, evtGetAO(event, 'keyboard'))
    event.Type = 'keyboard'
    wxCallAfter(self.OnGetAO, event)
    
  def OnClose(self, event):
    del self.hm
    self.Destroy()
  
if __name__ == '__main__':
  app = wxPySimpleApp(0)
  frame = myFrame()
  app.SetTopWindow(frame)
  frame.Show()  
  app.MainLoop()