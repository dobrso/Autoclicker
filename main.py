import pyautogui
import time


def click(x: int, y: int) -> None:
    pyautogui.moveTo(x, y)
    pyautogui.click()


def main() -> None:
    while True:
        click(100, 100)
        time.sleep(1)


if __name__ == "__main__":
    main()
