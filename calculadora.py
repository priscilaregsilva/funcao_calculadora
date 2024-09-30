#Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da 
#operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
#1. Soma
#2. Subtração
#3. Multiplicação
#4. Divisão

#Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

def calculadora(valor_1, valor_2, operacao):
    if operacao == 1:
        print("Soma: " , valor_1 + valor_2)
    
    elif operacao == 2:
        print("Subtração: " , valor_1 - valor_2)

    elif operacao == 3:
        print("Multiplicação: " , valor_1 * valor_2)

    elif operacao == 4:
        print("DIvisão: " , valor_1 / valor_2)
    else:
        print (0)


calculadora(5, 3, 1)