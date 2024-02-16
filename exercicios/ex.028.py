import random
pc = random.randint(0,5)
print('='*20)
print("ADIVINHE O NÚMERO")
print('='*20)
pens = int(input("Adivinhe o número inteiro entre 0 e 5 que estou pensando... "))

if pens == pc:
    print("Você venceu!!!")
else:
    print(f"Você perdeu eu pensei no número {pc} e não no {pens}!!!")