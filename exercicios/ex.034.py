sal = float(input("Qual o salário do funcionário? "))
if sal > 1250:
    porc = sal * (10/100)
    print(f"Um funcionário com o salário de R${sal} com o aumento passa a receber R${sal+porc:.2f}")
else:
    porc2 = sal * (15/100)
    print(f"Um funcionário com o salário de R${sal} com o aumento passsa a receber R${sal+porc2:.2f}")