print("="*20)
print("ANALISANDO TRIÂNGULOS")
print("="*20)
reta = float(input("Primeira reta: "))
reta2 = float(input("Segunda reta: "))
reta3 = float(input("Terceira reta: "))

if reta + reta2 > reta3 and reta2 + reta3 > reta and reta + reta3 > reta2:
    print("As retas acima podem formar um triângulo")
    if reta == reta2 == reta3:
        print(f"Essas retas formam um triângulo EQUILÁTERO ")
    elif reta != reta2 != reta3 != reta:
        print("Essas retas formam um triângulo ESCALENO")
    else:
        print("Essas retas formam um triângulo ISÓSCELES")
else:
    print("As retas acima não podem formar um triângulo")


