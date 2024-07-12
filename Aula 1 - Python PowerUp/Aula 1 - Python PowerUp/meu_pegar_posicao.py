import time
import pyautogui

time.sleep(5)
# permite possamos alternar para a tela a ser rastreada antes do processo ocorrer.
# primeiro você executa esse comando, alterna para o local desejado e espera o rastreamento
print(pyautogui.position()) 

pyautogui.scroll(200)