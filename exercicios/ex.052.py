cont = 0

num = int(input("Digite um número: "))

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;32m', end=" ")
        cont += 1
    else:
        print("\033[1;31m", end=" ")

    print(c, end=" ")

print('\033[m')

print(f"\nO número {num} foi dividido {cont} vezes")

if cont == 2:
    print("Ele é primo")
else:
    print("Ele não é primo")