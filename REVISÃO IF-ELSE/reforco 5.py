valor = float(input("Valor de compra: "))
vip = input("Cliente VIP? (S/N): ").strip().upper()

if valor < 0:
    print("Valor é inválido.")
else:
    if valor < 100:
        desconto = 0
    else:
        if valor < 300:
            desconto = 10
        else:
            if valor < 500:
                desconto = 15
            else:
                desconto = 20
    if vip == "S":
        desconto = desconto + 5
        if desconto > 25:
            desconto = 25
    else:
        if vip != "N":
            print("VIP inválido, considerando como N.")
    
    final = valor * (1 - desconto / 100)
    print(f"Desconto aplicado: {desconto}%")
    print(f"Total a pagar: R$ {final:.2f}")