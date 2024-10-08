#passo 1: https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time

#abrir navegador
pyautogui.PAUSE = 1
pyautogui.hotkey('win','r')
time.sleep(1)
pyautogui.write('msedge')
pyautogui.press('enter')