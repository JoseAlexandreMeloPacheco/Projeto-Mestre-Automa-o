import pyautogui
from time import sleep  

# Mover o cursor do mouse para a posição (1334, 433) com uma duração de 0,3 segundos
pyautogui.moveTo(1239,541, duration=0.3)

# Realizar 100 cliques, um a cada 0,5 segundos
for i in range(100):
    sleep(0.5)
    pyautogui.click()
