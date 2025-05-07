import time
import keyboard
import pyautogui as pag


def setRunning() -> None:
    global running
    running = not running


def clicker(x: int, y: int) -> None:
    pag.moveTo(x, y)
    pag.click()


def main() -> None:
    while running:
        x, y = pag.position()
        clicker(x, y)
        time.sleep(1)


keyboard.add_hotkey("=", setRunning)

running = True

if __name__ == "__main__":
    main()
