def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0

    for letra in texto:
        if letra in vogais:
            contador += 1

    return contador


print(contar_vogais("programacao"))