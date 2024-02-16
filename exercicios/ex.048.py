total = 0
cont = 0
for num in range (1,500+1,2):
    if num % 3 == 0:
        cont += 1
        total += num
print(f"A soma de todos os {cont} valores é {total}")

