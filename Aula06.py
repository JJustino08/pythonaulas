import os 
os.system("cls")
#ESTRUTURAS CONDICIONAIS IF ELSE (ELFIF)
# SWITCH CASE -> (match case) escolha caso ( a partir da versão 3.10 )
#match valor :

# linguagem = 100

# match linguagem:

#     case "python":
#         print("é facil")
#     case "java":
#         print("muito codigo , python faz com linhas menores")
#     case "c#":
#         print("massa")
#     case "js":
#         print("sou do back")
#     case "htmal":
#         print("kauan nao dorme")
#     case 10:
#             print("entrou aqui !")
#     case _ :
#         print()

# DIA DA SEMANA

# print("1 - SEGUNDA ")
# print("2 - TERÇA ")
# print("3 - QUARTA ")
# print("4 - QUINTA ")
# print("5 - SEXTA ")
# print("6 - SABÁDO ")
# print("7 - DOMINGO ")

# print("-------------------------------------")

# dia = input(" dia da semana: ")

# match dia:

#     case "1":
#         print(" Segunda-feira ")
#     case "2":
#         print(" Terça-feira ")
#     case "3":
#         print(" Quarta-feira ")
#     case "4":
#         print(" Quinta-feira ")
#     case "5":
#         print(" Sexta feira ")
#     case "6":
#             print(" Sabádo ")
#     case "7":
#         print(" Domingo ")

# print("""

#        (: CELULARES DO JOUNES :)

# """)
# print("""
# --------CELULARES--------      
# 1 - REDMAGIC 10 Pro / VALOR: R$ 4.899
# 2 - Samsung Galaxy S25 Ultra 5G / VALOR: R$ 10.799,10
# 3 - REDMI NOTE 13 5G / VALOR: R$ 1.500   
# """)
# print("""
#  ----------FRETE---------      
# SP -> 10,00
# MG -> 15,00
# RS -> 20,00    
# """)

# celular = float(input("DIGITE O NUMERO DO PRODUTO: "))

# match celular :

#     case "1":
#         print("VALOR: R$ 4.899 ")
#     case "2":
#         print("VALOR: R$ 10.799,10 ")
#     case "3":
#         print("VALOR: R$ 1.500 ")

# frete = float(input("DIGITE A SIGLA DO ESTADO: "))

# match frete :

#     case "SP":
#         print("VALOR DO FRETE: R$ 10,00 ")
#     case "MG":
#         print("VALOR DO FRETE: R$ 15,00 ")
#     case "RS":
#         print("VALOR DO FRETE: R$ 20,00 ")
#--------------------------------------------------------------
# print(""" 
# MUNDO CELULAR
      
# 1-IPHONE -> 5000
# 2-MOTO G -> 3000
# 3-LENOVO -> 2500

# FRETE: 
#       SP -> 10,00
#       RS -> 20,00
#       RJ -> 30,00      
# """)

# celular = int(input("Digite a opção desejada: "))
# estado = input("Digite a sigla do estado para entrega: ").lower()
# valor=0
# frete=0
# valortotal=0
# match celular:
#     case 1:
#         valor=5000
#     case 2:
#         valor=3000
#     case 3:
#         valor=2500

# match estado:
#     case "sp":
#         frete=10
#     case "rs":
#         frete=20
#     case "rj":
#         frete=30

# valortotal= valor + frete

# print(f"VALOR CELULAR:R$ {valor:.2f}")
# print(f"VALOR FRETE R$: {frete:.2f}")
# print(f"VALOR TOTAL R$: {valor+frete:.2f}")

# import random

# valor = 0
#randint(valorinicial,valorfinal)
# valor = random.randint(0,100) #gera de 1 ate 99 aleatoriamente

# match valor:

#     case _ if valor <50 : 
#         print("menor que 50")
#     case _ if valor ==50:
#         print("= 50")
#     case _ if valor > 50:
#         print("maior que 50")

#ATIVIDADE PEDRA PAPEL E TESOURA

import random

print("""
                 JOGO
----------PEDRA,PAPEL E TESOURA ----------

""")
opcoesj = input("ESCOLHA ENTRE PEDRA, PAPEL E TESOURA: ").lower()

pedra ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

papel = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

tesoura = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""

match opcoesj:

    case "pedra" :
        print(""" VOCE ESCOLHEU: 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""") 
    case "papel" :
        print(""" VOCE ESCOLHEU:
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    case "tesoura" :
        print(""" VOCE ESCOLHEU:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

""")

import random
pc = random.randint(1,3)

match pc :
    case _ if pc <= 3:
        print(""" O PC ESCOLHEU
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    case _ if pc >= 3:
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    case _ if pc == 3:
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

""")
        
match opcoesj:
    case _ if opcoesj == pc:
        print("""              

    ------EMPATE------

""")
    case _ if opcoesj <= pc:
        print("""              

    ------DERROTA------

""")
    case _ if opcoesj >= pc:
        print("""              

    ------ VENCEU ! ------

""")
        
#--------------------------------------------------------------


print("JOGO PEDRA PAPEL TESOURA")

papel = """
PAPEL
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

pedra = """
PEDRA
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


tesoura = """
TESOURA
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""

jogador = input("Escolha entre pedra, papel ou tesoura: ")
match jogador:
    case "pedra":
        jogador=pedra
    case "tesoura": 
        jogador =tesoura
    case "papel":
        jogador = papel

#1-> pedra , 2-> papel , 3->tesoura

maquina = random.randint(1,3)

match maquina:
    case 1:
        maquina=pedra
    case 2: 
        maquina =papel
    case 3:
        maquina =tesoura


print(f"voce escolheu  {jogador}")
print(f"maquina escolheu {maquina}")

match jogador:
    case _ if jogador == maquina:
        print("empate")
    case _ if jogador==pedra and maquina ==tesoura:
        print("Voce ganhou")
    case _ if jogador == tesoura and maquina ==papel:
        print("Voce ganhou")
    case _ if jogador == papel and maquina ==pedra:
        print("voce ganhou")
    case _ :
        print("voce perdeu")


print("2 MODO - PEDRA PAPEL TESOURA")


print("JOGO PEDRA PAPEL TESOURA ")

papel = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

pedra = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


tesoura = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""

#pedra=1 papel=2 tesoura=3
mao = input("Digite pedra ou papel ou tesoura :")
maquina = random.randint(1,3)

match maquina :
    case 1:
        maquina = "pedra"
    case 2:
        maquina = "papel"
    case 3 :
        maquina ="tesoura"

match mao:

    case _ if mao== "pedra" and maquina=="pedra" :
        print(f"Maquina: {maquina} {pedra}")
        print(f"Você: {mao}  {pedra}")
        print("EMPATOU!")
    
    case _ if mao== "pedra" and maquina=="papel":
        print(f"Maquina: {maquina} {papel}")
        print(f"Você: {mao}  {pedra}")
        print("PERDEU!")
    case _ if mao== "pedra" and maquina=="tesoura":
        print(f"Maquina: {maquina} {tesoura}")
        print(f"Você: {mao}  {pedra}")
        print("GANHOU!")
    case _ if mao== "papel" and maquina=="papel":
        print(f"Maquina: {maquina} {papel}")
        print(f"Você: {mao}  {papel}")
        print("EMPATOU!")
    case _ if mao== "papel" and maquina=="pedra":
        print(f"Maquina: {maquina} {pedra}")
        print(f"Você: {mao}  {papel}")
        print("GANHOU")
    case _ if mao== "papel" and maquina=="tesoura":
        print(f"Maquina: {maquina} {tesoura}")
        print(f"Você: {mao}  {papel}")
        print("PERDEU!")
    case _ if mao== "tesoura" and maquina=="pedra":
        print(f"Maquina: {maquina} {pedra}")
        print(f"Você: {mao}  {tesoura}")
        print("PERDEU!")
    case _ if mao== "tesoura" and maquina=="papel":
        print(f"Maquina: {maquina} {papel}")
        print(f"Você: {mao}  {tesoura}")
        print("GANHOU!")
    case _ if mao== "tesoura" and maquina=="tesoura":
        print(f"Maquina: {maquina} {tesoura}")
        print(f"Você: {mao}  {tesoura}")
        print("EMPATOU!")
    case _:
        print("DIGITOU ERRADO! ESCOLHA PAPEL OU TESOURA OU PEDRA")
