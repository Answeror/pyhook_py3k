import wx
from pyHookManager import *

class myFrame(wx.Frame):
  def __init__(self):
    wx.Frame.__init__(self, None, -1, 'My Frame')
    
    self.hm = HookManager()
    self.hm.MouseAllButtonsDown = self.OnMouseEvent
    self.hm.KeyDown = self.OnKeyboardEvent
  
    self.hm.HookMouse()
    self.hm.HookKeyboard()
    
    wx.EVT_CLOSE(self, self.OnClose)
  
  def OnMouseEvent(self, event):
    print 'MessageName:',event.MessageName
    print 'Message:',event.Message
    print 'Time:',event.Time
    print 'Window:',event.Window
    print 'WindowName:',event.WindowName
    print 'Position:',event.Position
    print 'Wheel:',event.Wheel
    print 'Injected:',event.Injected
    print '---'

  def OnKeyboardEvent(self, event):
    print 'MessageName:',event.MessageName
    print 'Message:',event.Message
    print 'Time:',event.Time
    print 'Window:',event.Window
    print 'WindowName:',event.WindowName
    print 'Key:', event.Key
    print 'KeyID:', event.KeyID
    print 'ScanCode:', event.ScanCode
    print 'Extended:', event.Extended
    print 'Injected:', event.Injected
    print 'Alt', event.Alt
    print 'Transition', event.Transition
    print '---'
      
  def OnClose(self, event):
    del self.hm
    self.Destroy()
  
if __name__ == '__main__':
  app = wx.PySimpleApp(0)
  frame = myFrame()
  app.SetTopWindow(frame)
  frame.Show()  
  app.MainLoop()