print("="*20)
print("ANALISANDO TRIÂNGULOS")
print("="*20)
reta = float(input("Primeira reta: "))
reta2 = float(input("Segunda reta: "))
reta3 = float(input("TErceira reta: "))
if reta + reta2 > reta3 and reta2 + reta3 > reta and reta + reta3 > reta2:
    print("As retas acima podem formar um triângulo")
else:
    print("As retas acima não podem formar um triângulo")