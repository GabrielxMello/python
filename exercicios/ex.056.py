
soma = 0
media = 0
maior = 0
velho = ''
mulher = 0

for pessoa in range(1,5):
    print(f"------ {pessoa}° ------")
    nome = str(input("Qual seu nome? ")).strip()
    idade = int(input("Qual sua idade? "))
    sexo = str(input("Qual seu sexo? [M/F] ")).strip()
    soma += idade
    if pessoa == 1 and sexo in 'Mm':
        maior = idade
        velho = nome
    if sexo in 'Mm' and idade > maior:
        maior == idade
        velho = nome
    if sexo in 'Ff' and idade < 20:
        mulher += 1



media = soma / 4
print(f"A média de idadendo grupo é {media} anos")
print(f"O homem mais velho tem {maior} anos e se chama {velho}")
print(f"Ao todo são {mulher} mulheres com menos de 20 anos")
