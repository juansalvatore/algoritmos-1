# Ejercicio 4.8. Programa de astrología: el usuario debe ingresar el día y mes de su cumpleaños
# y el programa le debe decir a qué signo corresponde.
# Acuario:      21 de enero al         19 de febrero. 
# Piscis:       20 de febrero al       20 de marzo.
# Aries:        21 de marzo al         20 de abril. 
# Tauro:        21 de abril al         20 de mayo.
# Geminis:      21 de mayo al          21 de junio.
# Cancer:       22 de junio al         23 de julio.
# Leo:          24 de julio al         23 de agosto.
# Virgo:        24 de agosto al        23 de septiembre.
# Libra:        24 de septiembre al    22 de octubre.
# Escorpio:     23 de octubre al       22 de noviembre.
# Sagitario:    23 de noviembre al     21 de diciembre.
# Capricornio:  22 de diciembre al     20 de enero.

def signo_sodiaco(dia, mes):
    signos = ["Capricornio", "Acuario", "Piscis", "Aries", "Tauro", "Geminis", "Cancer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario"]
    fechas = (21, 19, 20, 20, 20, 21, 23, 23, 23, 22, 22, 21)
    if dia < fechas[mes - 1]:
        return signos[mes - 1]
    return signos[mes % 12]


print(signo_sodiaco(22, 12))
