def cambio ():
    pesos = float (input())
    dolar = pesos *3.565
    euro =  pesos * 4.321
    yuan = pesos * 551.82

    valores = []
    valores.append(pesos)
    valores.append("PESOS")
    valores.append(dolar)
    valores.append("DOLARES")
    valores.append(euro)
    valores.append("EURO")
    valores.append(yuan)
    valores.append("YUANES")
    print(valores)
cambio()