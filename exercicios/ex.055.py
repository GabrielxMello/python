

pesom = 0
pesomn = float('inf')

for pessoa in range(1, 6):
    peso = float(input(f"Peso da {pessoa}ª pessoa: (kg) "))


    if peso > pesom:
        pesom = peso


    if peso < pesomn:
        pesomn = peso

print(f"O maior peso é {pesom} kg")
print(f"O menor peso é {pesomn} kg")
