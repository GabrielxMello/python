
soma = 0
cont = 0
for c in range (1,7):
    num = int(input("Dígite um número: "))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f"A somas dos {cont} números pares é igual a {soma}")
