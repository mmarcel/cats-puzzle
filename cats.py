import os
import sys
from bip32 import *

words = "blossom educate state course sick fresh color divide number soap please pull glide weather join grit depart dynamic tenant leopard alter piano slight room"

rockyou = "/usr/share/wordlists/rockyou.txt"
senhas = "senhas.txt"
#senhas = "vazio.txt"
cont = 0
WALLET = "bc1qcyrndzgy036f6ax370g8zyvlw86ulawgt0246r"
#WALLET_TESTE = "bc1q57euh23y3qs2f9d5mtwpax5lqecfvrdkqce82a"


with open(senhas, errors='ignore') as file:
    for line in file.readlines():
        line = line.strip()
        cont += 1
        if cont % 1 == 0:
            print(cont)
            print(line)

        resp = gera_dados_carteira(words, line)
        #resp = gera_dados_carteira("erase sausage virtual little gym eagle swift stone journey obtain parade")
        print(resp)
        if WALLET in resp:
            print("----ACHEI----")
            break
        