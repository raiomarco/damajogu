#coding: utf-8
import leitor
import processador

def damajogu(entrada):
    processado = processador.processar(entrada)
    exec(processado)

def exemplificador(entrada):
    print("ENTRADA\nVVVVVVV\n")
    print(entrada)
    print("^^^^^^^\n")

    processado = processador.processar(entrada)

    print("\nSAIDA\nVVVVV\n")
    exec(processado)
    print("\n^^^^^")

def main():
    try:
        entrada,exemplificar = leitor.ler()
        error = False
    except:
        print("Nenhum arquivo foi validado")
        error = True
    if not error:
        if exemplificar:
            exemplificador(entrada)
        else:
            damajogu(entrada)


main()
