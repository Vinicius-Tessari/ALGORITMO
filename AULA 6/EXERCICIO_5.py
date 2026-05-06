def saudacao_horario(horario):
    hora, minuto = horario.split(":")
    hora = int(hora)
    minuto = int(minuto)

    if hora < 0 or hora > 23 or minuto < 0 or minuto > 59:
        return "Horário inválido"

    if hora >= 5 and hora <= 11:
        return "Bom dia"
    elif hora >= 12 and hora <= 17:
        return "Boa tarde"
    else:
        return "Boa noite"


print(saudacao_horario("14:30"))
print(saudacao_horario("08:00"))
print(saudacao_horario("22:15"))
print(saudacao_horario("03:40"))