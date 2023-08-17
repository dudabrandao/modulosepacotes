def inverter_string(texto):
    return texto[::-1]

def maiusculas_minusculas(texto):
    return texto.upper(), texto.lower()

def substituir_substring(texto, antigo, novo):
    return texto.replace(antigo, novo)

def remover_espacos(texto):
    return texto.strip()

def contar_ocorrencias(texto, substring):
    return texto.count(substring)

def capitalizar_palavras(texto):
    return texto.title()

def centralizar_texto(texto, largura_total):
    return texto.center(largura_total)

def adicionar_zeros(numero, largura_total):
    return f"{numero:0>{largura_total}}"

def dividir_texto(texto, delimitador):
    return texto.split(delimitador)

def juntar_texto(lista_strings, separador):
    return separador.join(lista_strings)

def cor_texto(texto, cor):
    cores = {
        'vermelho': '\033[91m',
        'verde': '\033[92m',
        'amarelo': '\033[93m',
        'azul': '\033[94m',
        'roxo': '\033[95m',
        'reset': '\033[0m'
    }
    return cores.get(cor, '') + texto + cores['reset']