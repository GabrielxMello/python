nota = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota+nota2) / 2
if media < 5:
    print(f"Com as notas {nota} e {nota2} a média do aluno é {media}")
    print("ALUNO REPROVADO!!!")
elif media >= 5 and media < 7:
    print(f"Com as notas {nota} e {nota2} a média do aluno é {media}")
    print("ALUNO EM RECUPERAÇÃO!!!")
else:
    print(f"Com as notas {nota} e {nota2} a média do aluno é {media}")
    print("ALUNO APROVADO!!!")