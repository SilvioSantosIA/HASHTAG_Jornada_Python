# Passo a passo do projeto

# PASSO 1: entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui # biblioteca específica para interface gráfica.
import time # para ações que envolvam manipulação de tempo.

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar uma tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas (atalhos de teclado)

pyautogui.PAUSE = 0.3 # intervalo entre cada ação automatizada

# abrir o navegador (Chrome):
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link:
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# PASSO 2: fazer login
# selecionar o campo de e-mail
pyautogui.click(x=685, y=451) # essas não são as coordenada do meu computador; devem ser obtidas pelo arquivo meu_pegar_posicao.py

# escrever o seu e-mail
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # pressiona tecla TAB para ir para o próximo campo.
pyautogui.write("sua senha")
pyautogui.click(x=955, y=638) # coordenadas do botão de login
time.sleep(3)

# PASSO 3: cadastrar um produto
import pandas as pd

tabela = pd.read_csv("produtos.csv") # utilizando biblioteca do Pandas que lê .csv.

print(tabela)

# PASSO 4: cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=653, y=294)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o próximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs): # condição especial, pois nem todos os campos obs estão preenchidos
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # finaliza cadastra o produto (botão enviar)
    # dar scroll do cursor para o início da tela, para poder pegar o campo certo e cadastrar o produto seguinte.
    pyautogui.scroll(5000) # passar um valor alto para que o cursor volte realmente para o início da página

# PASSO 5: repetir o processo de cadastro até finalizar a lista.
