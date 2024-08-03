# Passo 1 - entrar no sistema da empresa
    # https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbTQzMUtCRHhBYkotVVV3eDlSNndGM05WelRJZ3xBQ3Jtc0ttck1lRnFqNllpUXJtNDFmdEtRVEVNdDVVanUzTmo0NzN2QjEzZ0FXOTFwTHE5Q3I2XzFmTnhwU3dVcWNNa0VfeS14ZktJX3VCSDdMMjFVc0s2bDhBY09HcndUekhXcWdmNG1sZHlHdFItMjJUYVFpaw&q=https%3A%2F%2Fdlp.hashtagtreinamentos.com%2Fpython%2Fintensivao%2Flogin&v=qbZsaBMxCJI
# Passo 2 - fazer login
# passo 3 - pegar a base de dados
# passo 4 - cadastrar os produtos
# passo 5 - repetir passo 4

import pyautogui
import time
pyautogui.PAUSE = 0.5
# Passo 1 - entrar no sistema
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=479, y=480)
pyautogui.click(x=659, y=58)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# passo 2 - login no sistema

time.sleep(3)
pyautogui.click(x=677, y=405)
pyautogui.write("pythonetop@gmail.com")
pyautogui.click(x=742, y=501)
pyautogui.write("12345678=D")
pyautogui.click(x=702, y=583)

# passo 3 - importar base de dados

import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)

# passo 4 - cadastrar os produtos

for linha in tabela.index:
    pyautogui.click(x=732, y=298)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    
    pyautogui.press("tab")
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)

    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)  

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(1000)

