import os
import sys
modules = os.path.abspath("../")
sys.path.append(modules)
from bip.bip32 import *

words = "blossom educate state course sick fresh color divide number soap please pull glide weather join grit depart dynamic tenant leopard alter piano slight room"

rockyou = "/usr/share/wordlists/rockyou.txt"
senhas = "senhas.txt"
cont = 0

#for i in open(senhas, errors='ignore').readlines():
with open(senhas, errors='ignore') as file:
    for line in file.readlines():
    #i = i.strip()
        line = line.strip()
        cont += 1
        if cont % 1 == 0:
            print(cont)
            print(line)
        #print(len(i))

        #passwd = ""
        resp = gera_dados_carteira(words, line)
        #resp = gera_dados_carteira("erase sausage virtual little gym eagle swift stone journey obtain parade")
        print(resp)
        if "bc1qcyrndzgy036f6ax370g8zyvlw86ulawgt0246r" in resp:
            print("ACHEI")
            break
        