import simpleM8
try:
	import wx
except ImportError:
	raise ImportError, "The wxPython module is required to run this program"

class M8_wx(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title)
		self.parent = parent
		self.initialize()

	def initialize(self):
		sizer = wx.GridBagSizer()

		self.entry = wx.TextCtrl(self, -1, value = u"Enter text here.", style=wx.TE_PROCESS_ENTER)
		sizer.Add(self.entry, (0, 0), (1, 3), wx.EXPAND)
		self.Bind(wx.EVT_TEXT_ENTER, self.OnPressEnter, self.entry)

		self.label = wx.StaticText(self, -1, label = u"Answer: ")
		sizer.Add(self.label, (1, 0), (1, 2), wx.EXPAND)

		button_ask = wx.Button(self, -1, label = "Ask")
		sizer.Add(button_ask, (2, 0))
		self.Bind(wx.EVT_BUTTON, self.OnButtonAskClick, button_ask)


		button_quit = wx.Button(self, -1, label = "Quit")
		sizer.Add(button_quit, (2, 2))
		self.Bind(wx.EVT_BUTTON, self.OnButtonQuitClick, button_quit)

		self.SetSizerAndFit(sizer)
		self.Show(True)

	def OnPressEnter(self, event):
		if self.entry.GetValue() != "Enter text here." and self.entry.GetValue() != "":
			self.label.SetLabel("Answer: " + simpleM8.M8_Play())
			self.entry.SetFocus()
			self.entry.SetSelection(-1, -1)

	def OnButtonAskClick(self, event):
		if self.entry.GetValue() != "Enter text here." and self.entry.GetValue() != "":
			self.label.SetLabel("Answer: " + simpleM8.M8_Play())
			self.entry.SetFocus()
			self.entry.SetSelection(-1, -1)

	def OnButtonQuitClick(self, event):
		self.Close()

if __name__ == "__main__":
	M8_ball = wx.App()
	frame = M8_wx(None, -1, "Magic 8 Ball")
	M8_ball.MainLoop()
