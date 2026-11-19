'''
Crie a estrutura de uma tabuada para um valor inserido. 
O resultado deverá ser printado do valor multiplicado de 1 a 10. 
'''
multiplicacao = int(input("Escreva um número para exibirmos sua multiplicação de 1 a 10 : "))

for i in range (1,11): 
    resultado = multiplicacao * i
    print(resultado)



