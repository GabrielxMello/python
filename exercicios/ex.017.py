from math import sqrt, pow

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
h = pow(co, 2) + pow(ca,2)
hipotenusa = sqrt(h)
print(f"A hipotenusa vai medir {hipotenusa:.2f}")