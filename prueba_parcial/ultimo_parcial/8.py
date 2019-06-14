def raiz_digital(n):
    total = 0
    if len(str(n)) == 1:
        return n
    total = int(str(n)[0])
    return total + raiz_digital(int(str(n)[1:]))

print(raiz_digital(342))