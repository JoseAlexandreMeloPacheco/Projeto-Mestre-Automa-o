import pyautogui
import pyperclip #permite digitar com carecteres epeciais, porém te que usar funçao

def escrever_frase(frase):
    pyperclip(frase)
    pyautogui.hotkey('ctrl','v') 

pyautogui.moveTo(1595,200, duration=2)
pyautogui.click()
pyautogui.sleep(3)
escrever_frase('Eu amo automação')


import pyautogui
from pyperclip import copy  # importa a função 'copy' do módulo 'pyperclip'

def escrever_frase(frase):
    copy(frase)  # copia a frase para a área de transferência
    pyautogui.hotkey('ctrl', 'v')  # cola a frase

pyautogui.moveTo(1595, 200, duration=2)
pyautogui.click()
pyautogui.sleep(1)  # adiciona um pequeno atraso para garantir que o clique seja registrado
escrever_frase('Eu amo automação')
