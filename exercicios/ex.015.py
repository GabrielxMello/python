dias = int(input("Quantos dias o carro foi alugado? "))
km = float(input("Quantos kilometros rodados nesses dias? "))
carro = dias * 60
kmr = km * 0.15
print(f"O total a pagar é de R${carro+kmr:.2f}")