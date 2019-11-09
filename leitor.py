import sys

def ler():
    arquivo = sys.argv[1]
    with open(arquivo, 'r', encoding="utf-8") as file:
        entrada = file.read()
    if "-e" in sys.argv:
        exemplificar = True
    else:
        exemplificar = False
    return entrada,exemplificar
