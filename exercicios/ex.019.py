import random
al1 = str(input("Primeiro aluno: "))
al2 = str(input("Segundo aluno: "))
al3 = str(input("Terceiro aluno: "))
al4 = str(input("Quarto aluno: "))
list = (al1, al2, al3, al4)
sorteando = random.choice(list)
print(f"A aluno sortedo foi {sorteando} ")
