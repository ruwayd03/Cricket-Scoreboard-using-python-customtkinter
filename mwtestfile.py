from tkinter import *
import webview
  
# define an instance of tkinter
tk = Tk()
  
#  size of the window where we show our website
tk.geometry("800x450")
  
# Open website
webview.create_window('Live Score', 'https://www.espncricinfo.com/live-cricket-score')
webview.start()