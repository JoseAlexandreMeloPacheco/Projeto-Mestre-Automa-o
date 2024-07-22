import pyautogui
from time import sleep


email = pyautogui.prompt(text='digite o seu email', title='Dados usuario')
sleep(1)
senha = pyautogui.password(text='digite o sua senha', title= 'dados usuario', mask='*')

print(email)
print(senha)

pyautogui.click(1626,291, duration=1)
sleep(1)
pyautogui.typewrite(email)
sleep(1)
pyautogui.hotkey('enter')
sleep(1)
pyautogui.typewrite(senha)



