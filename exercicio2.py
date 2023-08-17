#Exercício 2: Criando um Pacote
#Crie uma pasta chamada geometria no mesmo diretório em que seus arquivos estão localizados.
#Dentro da pasta geometria, crie um arquivo formas.py.
#Dentro de formas.py, crie funções para calcular a área de um círculo e de um quadrado.
#Crie um arquivo separado chamado app.py e importe o módulo geometria.formas.
#Peça ao usuário para escolher entre calcular a área de um círculo ou um quadrado e solicite os valores
#necessários. Utilize as funções do módulo geometria.formas para calcular e exibir a área.

from formas import *
area = str(input("Escolhe entre calcular a área do quadrado(a) ou calcular a área do círculo(b): "))
if area == "a":
    lateral= float(input("Digite a medida da lateral do quadrado: "))
    areaquadrado = area_quadrado(lateral)
    print(areaquadrado)
elif area == "b":
    raio= float(input("Digite o valor do raio do círculo: "))
    areacirculo = area_circulo(raio)
    print(areacirculo)

