import time
import keyboard
from PIL import ImageGrab


def screenshot():
    cur_time = time.strftime("_%Y%m%d_%H%M%S")
    screen = ImageGrab.grab()
    screen.save("screen{}.png".format(cur_time))


keyboard.add_hotkey("F8", screenshot)  # F1, ctrl+shift+s, a, b, ...

# esc 누를때까지 계속 실행, esc 종료
keyboard.wait("esc")
