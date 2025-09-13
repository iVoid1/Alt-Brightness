import threading
import keyboard, mouse
import screen_brightness_control as sbc
from PIL import Image
from pystray import Icon, MenuItem

key = "alt"

def on_scroll(event: mouse.WheelEvent):
    global current_brightness
    if type(event) != mouse.WheelEvent:
        return
    # نتأكد إن الزر Alt مضغوط
    if keyboard.is_pressed(key):
        sbc.set_brightness("+5" if event.delta > 0 else "-5")

def change_key():
    global key
    key = keyboard.read_key()

def on_exit_action(icon, item):
    icon.stop()
    print("Exiting.")
    
def main():
    mouse.hook(on_scroll)
    mouse.wait()    
    image = Image.open("icon.png")
    
    
    menu = (MenuItem('Change key', change_key),MenuItem('Exit', on_exit_action))
    
    icon = Icon("Brightness_Controller", image, "Brightness Controller", menu)
    
    icon.run()

if __name__ == "__main__":
    main()