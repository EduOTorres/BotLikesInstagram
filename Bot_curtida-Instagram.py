import pyautogui
import webbrowser
from time import sleep

nome_usuario = pyautogui.prompt(text= 'Insira seu usuário', title= 'Usuário')
senha = pyautogui.password(text = 'Insira sua senha', title= 'Senha', mask = '*')
pagina = pyautogui.prompt(text= 'Insira a página desejada')
mensagem = pyautogui.prompt(text= 'Insira a mensagem que gostaria de comentar', title = 'comentário')

webbrowser.open('https://www.instagram.com')
sleep(3)
#clicar para tirar o verme do gilberto
pyautogui.click(1457,687, duration= 1)

#logar usuário
pyautogui.click(1431,381, duration= 1)
pyautogui.typewrite(nome_usuario)

#logar senha
pyautogui.click(1428,442, duration= 1)
pyautogui.typewrite(senha)


pyautogui.click(1462,500, duration= 1)
sleep(4)

pyautogui.click(1455,715, duration= 0.5)
sleep(3)

pyautogui.click(1564,179, duration= 0.5)
pyautogui.typewrite(pagina)
pyautogui.click(1650,268, duration= 1)
sleep(3)

pyautogui.click(1150,870, duration= 0.5)
sleep(3)
pyautogui.scroll(-1000)
pyautogui.click(1280,908, duration= 1)
pyautogui.click(1325,925, duration= 1)
sleep(3)
pyautogui.scroll(-1000)
pyautogui.click(1325,925, duration= 1)

pyautogui.typewrite(mensagem)
pyautogui.press('Enter')
sleep(1)

pyautogui.press('Esc')
pyautogui.click(1047,175, duration= 1)

