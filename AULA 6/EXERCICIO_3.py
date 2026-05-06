def calcular(numeros):
    soma = sum(numeros)
    media = soma / len(numeros)

    return soma, media


print(calcular([2, 4, 6]))