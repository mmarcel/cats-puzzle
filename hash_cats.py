import os
import sys
modules = os.path.abspath("../")
sys.path.append(modules)
from bip32_utils import *

import hashlib

words = "blossom educate state course sick fresh color divide number soap please pull glide weather join grit depart dynamic tenant leopard alter piano slight room"

rockyou = "/usr/share/wordlists/rockyou.txt"
senhas = "senhas.txt"
#senhas = "vazio.txt"
cont = 0
WALLET = "bc1qcyrndzgy036f6ax370g8zyvlw86ulawgt0246r"
#WALLET = "bc1qlrqp820x7msf0alwskxequfw9kg868pkdku743"

#texto = "The mnemonic for the kitten photo without a passphrase contains roughly 0.00095133 BTC. Feel free to claim it if you manage to sweep the keys in time. As a challenge, I have also sent 0.01 BTC to the following address, “bc1qcyrndzgy036f6ax370g8zyvlw86ulawgt0246r”. This address was generated using the kitten image along with a BIP39 passphrase. If you manage to claim it, congrats!"
#texto = "CATS"

#hash_obj = hashlib.sha256(texto.encode())
#hash_hex = hash_obj.hexdigest()
#print("SHA-256:", hash_hex)

with open(senhas, errors='ignore') as file:
    for line in file.readlines():
        line = line.strip()
        hash_obj = hashlib.sha256(line.encode())
        hash_hex = hash_obj.hexdigest()
        cont += 1
        if cont % 1 == 0:
            print(cont)
            print(line)
            print(hash_hex)

        hash = gera_dados_carteira(words, hash_hex)
                #resp = gera_dados_carteira("erase sausage virtual little gym eagle swift stone journey obtain parade")
        passwd = gera_dados_carteira(words, line)
        #print(resp)
        if WALLET in hash or WALLET in passwd:
            print("----ACHEI----")
            break



        