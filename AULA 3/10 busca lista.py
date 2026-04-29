nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Juliana"]
busca = input("Digite um nome: ").strip().lower()
encontrado = False

for nome in nomes:
    if nome.lower() == busca:
        encontrado = True

if encontrado:
    print("Encontrado")
else:
    print("Não encontrado")
