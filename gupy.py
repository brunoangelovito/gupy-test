def calc_soma(indice):
    soma = 0
    k = 0
    while k < indice:
        k += 1
        soma += k
    return soma

soma = calc_soma(13)
print(f"a soma é : {soma}")
