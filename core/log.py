import logging
import sys
import wx

class LogWindow(wx.Frame):
    def __init__(self, main_window):
        super().__init__(parent=None, title="Logger", size=(400, 300))
        self.main_window = main_window
        self.populate_window()
        
        self.log = logging.getLogger()
        self.log.setLevel(logging.INFO)
        
        self.handler = Handler(self)
        self.handler.setLevel(logging.INFO)
        self.handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        
        self.console_handler = logging.StreamHandler(sys.stdout)
        self.console_handler.setLevel(logging.INFO)
        self.console_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        
        self.Bind(wx.EVT_CLOSE, self.on_close)
    
    def populate_window(self) -> None:
        self.scroll_win = wx.ScrolledWindow(self, style=wx.VSCROLL)
        self.log_ctrl = wx.TextCtrl(self.scroll_win, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.scroll_win.SetSizer(wx.BoxSizer(wx.VERTICAL))
        self.scroll_win.GetSizer().Add(self.log_ctrl, 1, wx.EXPAND | wx.ALL, border=5)

        # Set the scrolled window as the main sizer of the frame
        self.SetSizer(wx.BoxSizer(wx.VERTICAL))
        self.GetSizer().Add(self.scroll_win, 1, wx.EXPAND)
        
    def clean(self):
        self.scroll_win.Clear()
        self.populate_window()
    
    def log_message(self, message: str):
        try:
            self.log_ctrl.AppendText(message + '\n')
        except RuntimeError as e:
            if str(e) == "wrapped C/C++ object of type TextCtrl has been deleted":
                # Error comes up in jupyter notebooks because of stale GUI references and can be savely ignored
                pass
            else:
                raise
    
    def on_close(self, event):
        self.main_window.log_window = None
        self.Destroy()

    
class Handler(logging.StreamHandler):
    def __init__(self, log_window):
        super().__init__()
        self.log_window = log_window
    
    def emit(self, message) -> None:
        message = self.format(message)
        self.log_window.log_message(message)
    