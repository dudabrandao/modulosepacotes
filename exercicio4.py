#Exercício 4: Conversor de Unidades
#Crie um pacote chamado conversor_unidades.
#Dentro desse pacote, crie um módulo chamado conversao e defina funções para
#converter entre unidades, como Celsius para Fahrenheit.
#No mesmo diretório, crie um arquivo chamado main.py.
#Importe as funções do módulo conversor_unidades.conversao no main.py.
#Crie um programa que permita ao usuário converter entre unidades.

from conversor import *
graus = str(input("Digite para qual unidade de medida você deseja converter: Celsius(c) ou Fahrenheit(f): "))
if graus == "c":
    valor1 = float(input("Digite o valor da temperatura: "))
    valorconvertido1 = conversor_temperatura1(valor1)
    print(valorconvertido1)
elif graus == "f":
    valor2 = float(input("Digite o valor da temperatura: "))
    valorconvertido2 = conversor_temperatura2(valor2)
    print(valorconvertido2)
