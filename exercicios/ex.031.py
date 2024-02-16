dist = float(input("Qual a distãncia da sua viajem? "))
if dist <= 200:
    via1 = dist * 0.50
    print(f"Sua viajem de {dist}km vai custar R${via1:.2f}")
else:
    via2 = dist * 0.45
    print(f"sua viajem de {dist}km vai custar R${via2:.2f}")