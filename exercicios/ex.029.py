vel = float(input("Qual velocidade você estavá? "))
if vel >= 80:
    mult = (vel-80) * 7
    print("MULTA: Sua velocidade estava acima do aceito ")
    print(f"Com a velocidade de {vel}km/h, sua multa vai custar R${mult:.2f}")
else:
    print("Você é um ótimo condutor, continue assim!!!")
