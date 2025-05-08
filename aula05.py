import os 
os.system("cls")
#IF ENCADEADO -> TESTA TODAS AS CONDIÇÕES MESMO SE UMA FOR VERDADEIRA
#ELIF -> TESTA TODAS AS CONDIÇÕES ATÉ UMA SER VERDADEIRA


# x = 15 

# if x <=20 :
#     print("entrou no if 14")
# if x <=15 :
#     print("entrou no if 15")
# if x <=16:
#     print("entrou no if 16")


# if x <=20:
#     print("entrou no if 14")
# elif x<=15:
#     print("entrou no if 15")
# elif x <=16:
#     print("entrou no if 16")


# ESCREVA UM PROGRAMA EM PYTHON NA QUAL O USUARIO DIGITA A IDADE
#  SE MENOR QUE 12 -> CRIANÇA
#  SE MENOR QUE 18 -> ADOLESCENTE
#  SE MENOR QUE 60 -> ADULTO
#  SE NAO -> IDOSO


# NO CASO SE USAR IF ELE VAI TESTAR TODAS AS CONDIÇÕES
# idade = int(input("digite sua idade: "))

# if idade < 12:
#     print("criança")
# if idade < 18:
#     print("adolescente")
# if idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")


# SE USAR ELIF ELE VAI TESTAR UMA E SAIR DA ESTRUTURA
# if idade < 12:
#     print("criança")
# elif idade < 18:
#     print("adolescente")
# elif idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")



#ATIVIDADE 1

#replace("valor1","valor2") -> subistitui o valor1 pelo valor2 

# n1 = float(input("Digite a 1 nota ").replace(",","."))
# n2 = float(input("Digite a 2 nota ").replace(",","."))

# m = (n1 + n2)/2
# #:.f -> formata para 2 casas decimais apenas no fstring
# print(f"Média: {m:.2f}")

# if m <5 :
#     print("Reprovado")
# elif  m > 5 :
#     print("Aluno em recuperação")
# elif m > 7 :
#     print("Aprovado")

#ATIVIDADE 2

# p = float(input("Digite seu peso: "))
# a = float(input("Digite sua altura: "))

# imc = round((p / (a * a)),2)

# print(f"seu IMC é: {imc}")

# if imc < 17 :
#     print("Muito abaixo do peso ")
# elif imc <= 18.59 :
#     print("Abaixo do peso ")
# elif imc <= 24.99 :
#     print("Peso normal ")
# elif imc <= 29.99 :
#     print("Acima do peso ")
# elif imc <= 34.99 :
#     print("Obsidade I ")
# elif imc <= 39.99 :
#     print("Obseidadde II ")
# else :
#     print("Obesidade 3 (mórbida)")
# elif imc > 40 :
#     print("Obesidade III (mórbida) ")

#ATIVIDADE 3

print(r""" 
             #######                           
           ###      ###                        
         ###           ##                      
        ##              ###############        
       ##                   #       #####      
      ##                                ###    
     ##                                   ##   
    ##                   ##                ##  
    ##                   ##                 #  
   ##                    #                  #  
   ##   ##                                  #  
  ##  # #####                               ## 
  ## #########                              ###
  #  #########                              ###
  # ############                           ##  
  # ### ### ## ##                         ##   
  # ## ######## #                       ##     
  # ##  ####### ##   ##              ####      
  # ##  ####### ##    #           ####         
  # #######  ## ##     ####   #####            
   # ######  ## #          ####                
   ##  #######  ####      ###                  
    ##   ###   ######    ##                    
     ###     ###    #     ###                  
        ######     #########                   
                    ##     ##                  
                    #       ##                 
                    #        ##                
                   ##         ##               
                   #    ##     ##              
                  ##    ##      ##             
                  # #    #       ##            
                 ## #    ##      ##            
           ####  ## #     #      ##            
            ####### #     #      ##            
             ##  # #      #     ###   ###      
               ### #   #  #     ##  ### ##     
             ##  # ##  # ##   ##   ##    ##    
            ####  # #####     ##  ##     ##    
           ##  ####            ###       ##    
           ##   ##    #####     #     # ##     
            #        #    #            ##      
            #       ##    ##      ##   ##      
            ##       ##   ##        ####       
             ##       ## ##         ##         
             ##  ##    ##         ##           
              ## ## #  #       ####            
               ###  #####  #####               
                 #####  #####                  
""")




s = float(input("Digite seu salario: "))

if s <= 2799.99 :
    s*0.20 + 2799.99
    print("Aumento de 20% ")
elif s <= 6999.99 :
    s*0.15+ 6999.99
    print("Aumento de 15% {s}")
elif s <= 14999.99 :
    s*0.10+14999.99
    print("Aumento de 10% ")
elif s > 15000.00 :
    s*0.05+15000.00
    print("Aumento de 5% ")

v1 =s*0.20 
v2 =s*0.15
v3 =s*0.10
v4 =s*0.05