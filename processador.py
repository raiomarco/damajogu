def corretor(dict):
    dict = {
    "print": dict["print"],
    "if ": dict["if"]+" ",
    "elif ": dict["elif"]+" ",
    "else": dict["else"],
    "while ": dict["while"]+" "
    }
    return dict

def processar(entrada):

    import importlib
    language = entrada.split("\n")[0].replace("#!dict=","")
    dict = importlib.import_module('dicts.language'.replace("language",language)).dict
    dict = corretor(dict)

    processamentoEntrada = entrada.split('"')
    processado = []
    bagulho = True

    for i in processamentoEntrada:

        if bagulho:
            andamento = i
            for j in dict:
                andamento = andamento.replace(dict[j],j)
            processado.append(andamento)
            bagulho = False
        elif not bagulho:
            processado.append(i)
            bagulho = True

    processado = '"'.join(processado)
    return processado
