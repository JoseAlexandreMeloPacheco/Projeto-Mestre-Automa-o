import pyautogui
import webbrowser
import pyperclip
from time import sleep

login = 'meu login'
senha = 'minha senha'
comentario = 'muito bom'


url = 'https://www.instagram.com'
entrar = pyautogui.locateAllOnScreen

webbrowser.open_new(url)
sleep(5)
pyautogui.click(1228,146,duration=2)

pyautogui.click(1011,692,duration=2)

pyautogui.click(870,440,duration=2)

pyautogui.typewrite(login)

pyautogui.hotkey('tab')

pyautogui.typewrite(senha)

pyautogui.click(898,528,duration=2)
sleep(7)
pyautogui.click(83,294,duration=2)
sleep(1)
pyautogui.click(190,227,duration=2)
sleep(1)
pyautogui.typewrite('nike')
sleep(1)
pyautogui.click(242,282,duration=2)
sleep(3)
pyautogui.click(775,732, duration=1)
sleep(3)
pyautogui.click(1216,1003, duration=1)
sleep(2)
pyautogui.typewrite(comentario)
sleep(1)
pyautogui.click(1490,1001)
sleep(2)
pyautogui.moveTo(1107,910)
pyautogui.click(1107,910)
