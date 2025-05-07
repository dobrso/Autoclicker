import time
import keyboard
import pyautogui as pag


def setRunning() -> None:
    global running
    running = not running


def setClicking() -> None:
    global clicking
    clicking = not clicking


def clicker(x: int, y: int) -> None:
    pag.moveTo(x, y)
    pag.click()


def main() -> None:
    while running:
        if clicking:
            x, y = pag.position()
            clicker(x, y)
            time.sleep(1)


keyboard.add_hotkey("=", setRunning)
keyboard.add_hotkey("-", setClicking)

running = True
clicking = False

if __name__ == "__main__":
    main()
