#Exercício 1: Importando e Usando Módulos
#Crie um arquivo chamado calculadora.py.
#Dentro desse arquivo, defina funções para adição, subtração, multiplicação e divisão.
#Crie um arquivo separado chamado main.py e importe o módulo calculadora.
#Peça ao usuário para inserir dois números e uma operação (+, -, *, /).
#Com base na operação inserida, chame a função correspondente do módulo calculadora e exiba o resultado.

from calculadora import *
numero1= int(input("Digite um número inteiro: "))
numero2= int(input("Digite um outro número inteiro: "))
operacao= str(input("Escolha uma operação entre as seguintes: Soma(+), Subtração(-), Multiplicação(*), Divisão(/): "))
if operacao == "+":
    soma1 = soma(numero1, numero2)
    print(soma1)
elif operacao == "-":
    subtracao1 = subtracao(numero1, numero2)
    print(subtracao1)
elif operacao == "*":
    multiplicacao1 = multiplicacao(numero1, numero2)
    print(multiplicacao1)
elif operacao == "/":
    divisao1 = divisao(numero1, numero2)
    print(divisao1)