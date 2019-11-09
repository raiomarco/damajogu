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

    from dict import dict
    dict = corretor(dict)

    processamento1 = entrada.split('"')
    processado = []
    bagulho = True

    for i in processamento1:

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
