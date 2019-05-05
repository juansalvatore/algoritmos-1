# Ejercicio 11.5. Crear las clases Materia y Carrera, que se comporten según el siguiente ejemplo:

# >>> analisis2 = Materia("61.03", "Análisis 2", 8)
# >>> fisica2 = Materia("62.01", "Física 2", 8)
# >>> algo1 = Materia("75.40", "Algoritmos 1", 6)
# >>> c = Carrera([analisis2, fisica2, algo1])
# >>> str(c)
# Créditos: 0 -- Promedio: N/A -- Materias aprobadas:
# >>> c.aprobar("95.14", 7)
# ValueError: La materia 75.14 no es parte del plan de estudios
# >>> c.aprobar("75.40", 10)
# >>> c.aprobar("62.01", 7)
# >>> str(c)
# Créditos: 14 -- Promedio: 8.5 -- Materias aprobadas:
# 75.40 Algoritmos 1 (10)
# 62.01 Física 2
