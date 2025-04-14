import wx

from gui.frame import Frame

class App(wx.App):
    def __init__(self):
        self.simulation = None
        super().__init__(False)
        wx.HandleFatalExceptions()
    
    def OnInit(self):
        self.frame = Frame(None, "PyBEAST++", simulation=self.simulation)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
    

if __name__ == "__main__":
    app = App()
    app.MainLoop()