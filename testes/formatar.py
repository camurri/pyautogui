import pyautogui as auto
import time
import pandas


auto.PAUSE = 0.5

auto.press("win")
auto.write("chrome")
auto.press("enter")

auto.PAUSE = 0.3

auto.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

auto.press("enter")
time.sleep(3)

auto.press("tab")
auto.write("pirolinha@hotmail.com")
auto.press("tab")
auto.write("minhasenha")

auto.press("enter")
time.sleep(3)
print("ok")

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:

    auto.click(x=751, y=330)

    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    auto.write(str(codigo))
    # passar para o proximo campo
    auto.press("tab")
    # preencher o campo
    auto.write(str(tabela.loc[linha, "marca"]))
    auto.press("tab")
    auto.write(str(tabela.loc[linha, "tipo"]))
    auto.press("tab")
    auto.write(str(tabela.loc[linha, "categoria"]))
    auto.press("tab")
    auto.write(str(tabela.loc[linha, "preco_unitario"]))
    auto.press("tab")
    auto.write(str(tabela.loc[linha, "custo"]))
    auto.press("tab")

    obs =  tabela.loc[linha, "obs"]
    if obs != "nan":
        auto.write(str(obs))
        auto.press("enter")

    auto.scroll(10000)

  
   
