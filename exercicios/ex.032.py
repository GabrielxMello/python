print("="*20)
print("BISSEXTO OU NÃO")
print("="*20)
ano = int(input("Que ano quer analisar? "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano de {ano} é bissexto")
else:
    print(f"O ano de {ano} não é bissexto")