import os
os.system("cls")

#ESTRUTURA CONDICIONAL IF ELSE (se senao) -> True or False (Verdadeiro ou Falso)
#OPERADORES CONDICIONAIS:  > >= < <= != == and or
# > (maior)
# >= ( maior OU igual)
# < (menor)
# <= (menor OU igual)
# == (igual) 
# != (diferente)
# and (e) -> Se apenas uma ou mais condiçoes for FALSA ele retorna FALSE 
# or (ou) -> Se apenas uma ou mais condições for VERDADE ele retorna TRUE

#if condicao :
# print("verdade")
#else: 
#print("falso")

# A IDENTAÇÃO (ESPAÇO) deve ser utilizado o TAB

# if tot<100:
#     print("vocêé incrivel")
# else:
#     print("você é vacilão")

# x=10  

# if x > 1000:
#      print("verdade")
# else:
#     print("falso")
#     print("falso")     
#     print("falso")
#     print("falso")

# nome = "teste"
# if "testee" != nome:
#     print(1)
# else:
#     print(2)

#exercicio if else

#1-
# x1 = float(input("digite sua idade "))
# if x1 <= 17:
#      print("menor de idade")
# else:
#     print("maior de idade")

#2-
# idade = float(input("digite sua idade "))
# if idade <= 17:
#     print("idade invalida")
# else:
#     print("idade valida")
# if idade >= 18: 
#      print("validido")
# if idade <= 17:
#      print("invalido")
#  if idade >= 120:
#      print("invalido")

#3-

# email = input(print("digite seu o email: "))
# senha = input(print("digite sua senha: "))
# if email == "python@senai.com":
#      print("USUARIO AUTENTICADO")
# else:
#      print("usuario invalido")
    
# print("="*10, "MAÇANEIRAS BOA MAÇA AQUI","="*10)
# print("R$:0.30 -> MENOS QUE UMA DUXIA")
# print("R$:0.25 -> PELO MENOS DOZE")
# pro1 = input("QUANTAS MAÇAS VOCE QUER COMPRAR: ")
# preço1 = int(0.30)
# preço2 = int(0.25)
# desc1 = round(pro1 - pro1,2)
# print("----------------------")
# print("="*10, "VALOR","="*10)
# print("o valor do produto com desconto de 10% é ", round(val1-desc1,2))
# print("o valor do protudo com desconto de 25% é ", round(val2 -desc2,2))
# print("----------------------")
# print("#"*10, "TOTAL","#"*10)
# print("O TOTAL É ", round(tot,2))
# print("----------------------")


#ATIVIDADE DA MAÇA 

qtd = int(input("digite a qtd de maças que deseja levar"))

if qtd < 12:
    calc = qtd * 0.30
    print("voce ira pagar (0,30 a uni) R$: " , calc)
else :
    calc = qtd * 0.25
print("voce ira pagar (0,25 a uni) R$: " , calc)

#ATIVIDADE 1

# vogais = input("digite uma letra: ")
# if vogais == "a" or vogais == "e" or vogais == "i" or vogais == "o" or vogais == "u" == "A" or vogais == "E" or vogais == "I" or vogais == "O" or vogais == "U" or vogais:
#     print("É vogal ")

# else :
#    print("essa letra é consoante")

#reescrevendo de outra maneira 2

# vogais = input("digite uma letra: ").lower ou upper()
# if vogais == "a" or vogais == "e" or vogais == "i" or vogais == "o" or vogais == "u" == "A" or vogais == "E" or vogais == "I" or vogais == "O" or vogais == "U" or vogais:
#      print("É vogal ")

# else :
#     print("essa letra é consoante")

#reescrevendo de outra maneira 3

vogais = input("digite uma letra: ")
if vogais in "aeiouAEIOU" :
    print("vogal")
else :
    print("consoante")

#ATIVIDADE 2

# num1 = float(input("digite um numero: "))
# num2 = float(input("digite outro numero: "))

# if num1 > num2 :
#     print("esse numero é maior",num1)

# else :
#     print("esse numero é menor" , num2)
