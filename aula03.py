import os
os.system("cls")

#continuação input com int e float
#int() -> converte para inteiro
#float() -> converte numero quebrado
#exemplo1
# numero = 10
# numero2 = input("digite um numero:")
# print("o tipo de numero é,", type (numero2))
# soma = numero + int(numero2)
# print(f"soma de {numero} + {numero2} = ", soma )

#exemplo2
# num1 = input("digite um numero")
# soma = float(num1) + 10
# print("a soma de ",num1 , "+", "15" , "=", soma)

#exemplo3
# n1 = float(input("digite outo numero: "))
# n2 = float(input("digite outro numero: "))

# soma = n1+n2

# print(f'a soma de {n1} + {n2} = ', soma)

#exercicio1
# n1 = float(input("digite um numero: "))
# n2 = float(input("digite outro numero: "))
# mul= n1*n2
# print(f'a multiplicação de {n1} + {n2} = ', mul)

#exercicio2
# n1 = float(input("digite um numero: "))
# ant = n1 - float(1)
# suc = n1 + float(1)
# print(f"o sucessor é {suc}")
# print(f"o antecessor é {ant}")

#exercicio3
# n1 = float(input("digite o ano do seu nascimento "))
# idade = float(2025) - n1
# print(f'sua idade é = {idade} ')

#supondo que um produto custa 150 reais
#e o caixa deu um dsconto de 15%
# exemplo = float(input("digite o preço do produto: "))
# desconto = 0.15 * exemplo
# print("o preço do produtocom 15% de desconto é ", exemplo-desconto)



print("="*10, "CAIXA","="*10)
pro1 = input("digite o nome do produto: ")
val1 = float(input("valor do produto: "))
pro2 = input("digite o nome do outro produto: ")
val2 = float(input("valor do produto: "))
desc1 = round(0.10 * val1,2)
desc2 = round(0.25 * val2,2)
tot = val1 - desc1 + val2 - desc2
print("----------------------")
print("="*10, "VALOR","="*10)
print("o valor do produto com desconto de 10% é ", round(val1-desc1,2))
print("o valor do protudo com desconto de 25% é ", round(val2 -desc2,2))
print("----------------------")
print("#"*10, "TOTAL","#"*10)
print("O TOTAL É ", round(tot,2))
print("----------------------")
# if tot<100:
#     print("vocêé incrivel")
# else:
#     print("você é vacilão")

#round(valor,quantidade de casas decimais) 
# -> faz o arredondamento dos valores
 






