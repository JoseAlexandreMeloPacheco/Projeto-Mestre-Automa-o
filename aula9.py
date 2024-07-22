import pyautogui

captchar = pyautogui.locateCenterOnScreen('Sem.png')
pyautogui.click(captchar[0], captchar[1], duration=2)

