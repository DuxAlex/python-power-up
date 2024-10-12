#passo 1: https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time
import pandas

#1. abrir navegador
pyautogui.PAUSE = 1
pyautogui.hotkey('win','r')
time.sleep(1)
pyautogui.write('msedge')
pyautogui.press('enter')

#2. fazer login
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

#click
time.sleep(5)
pyautogui.click(x=-833, y=393)
pyautogui.write('email@email.br')
pyautogui.hotkey('tab')
#pyautogui.click(x=-833, y=493)
pyautogui.write('senha123')
#pyautogui.click(x=-828, y=551)
pyautogui.hotkey('tab','enter')
time.sleep(1)

#3. importa base de dados
#pip install pandas
#import pandas
tabela = pandas.read_csv ("produtos.csv")

linha = 0
for linha in tabela.index:
    pyautogui.click(x=-834, y=291)
    #codigo
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(str(codigo))
    pyautogui.hotkey('tab')

    #marca
    marca = tabela.loc[linha,"marca"]
    pyautogui.write(str(marca))
    pyautogui.hotkey('tab')

    #tipo
    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(str(tipo))
    pyautogui.hotkey('tab')

    #categoria
    categoria = tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.hotkey('tab')

    #preco_unitario
    preco_unitario = tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.hotkey('tab')

    #custo
    custo = tabela.loc[linha,"custo"]
    pyautogui.write(str(custo))
    pyautogui.hotkey('tab')

    #obs
    obs = tabela.loc[linha,"obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
        pyautogui.hotkey('tab')
    else:
        pyautogui.write('Sem observações')
    pyautogui.press('enter')

    #continuar processo
    pyautogui.scroll(5000)
    pyautogui.click(x=-834, y=291)

