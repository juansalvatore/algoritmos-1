# Ejercicio 4.5. Escribir funciones que resuelvan los siguientes problemas:
# a) Dado un año indicar si es bisiesto.
# Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100,
# excepto que también sea divisible por 400.
# b) Dado un mes, devolver la cantidad de días correspondientes.
# c) Dada una fecha (día, mes, año), indicar si es válida o no.
# d) Dada una fecha, indicar los días que faltan hasta fin de mes.
# e) Dada una fecha, indicar los días que faltan hasta fin de año.
# f) Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha.
# g) Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido
# entre ambas, en años, meses y días.
# Nota: en todos los casos, invocar las funciones escritas previamente cuando sea posible

def es_bisiesto(anio):
    if(anio % 4 == 0 and anio % 400 == 0):
        return True
    if(anio % 4 == 0 and anio % 100 == 0):
        return False
    if(anio % 4 == 0):
        return True
    return False

# print(es_bisiesto(2004))

def mes_a_dias(mes):
    if (mes == 2): 
        return 28
    if(mes in [1, 3, 5, 7, 8, 10, 12]):
        return 31
    if(mes in [4, 6, 9, 11]):
        return 30
    return 'no es un mes'

# print(mes_a_dias(1))

def fecha_es_valida(dia, mes, anio):
    if mes < 1 or mes > 12:
        return False
    if mes == 2 and es_bisiesto(anio):
        return mes_a_dias(mes) + 1 >= dia > 0
    return mes_a_dias(mes) >= dia > 0

# print(fecha_es_valida(29, 2, 2004))

def dias_para_fin_de_mes(dia, mes, anio):
    if not fecha_es_valida(dia, mes, anio):
        return 'La fecha no es valida'
    if mes == 2 and es_bisiesto(anio):
        return (mes_a_dias(mes) + 1) - dia
    return mes_a_dias(mes) - dia

# print(dias_para_fin_de_mes(29, 2, 2004))

def dias_para_fin_de_anio(dia, mes, anio):
    if not fecha_es_valida(dia, mes, anio):
        return 'La fecha no es valida'
    dias_restantes = 0
    for i in range(mes, 13):
        dias_restantes += mes_a_dias(i)
    return dias_restantes - dia

# print(dias_para_fin_de_anio(31, 1, 1994))

def dias_transcurridos_en_anio(dia, mes, anio):
    if not fecha_es_valida(dia, mes, anio):
        return 'La fecha no es valida'
    dias_restantes = dias_para_fin_de_anio(dia, mes, anio)
    if es_bisiesto(anio):
        return 366 - dias_restantes
    return 365 - dias_restantes

# print(dias_transcurridos_en_anio(2, 1, 2004))

def modulo(n):
    return int(((n)**2)**(1/2))

def tiempo_transcurrido_entre_fechas(dia1, mes1, anio1, dia2, mes2, anio2):
    dias = modulo(dia1 - dia2)
    meses = modulo(mes1 - mes2)
    anios = modulo(anio1 - anio2)
    return f"{dias} dias {meses} meses {anios} años"

print(tiempo_transcurrido_entre_fechas(22,1,1994, 1,12,1991))