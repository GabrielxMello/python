
from datetime import date

atual = date.today().year
totm = 0
totmn = 0
for hum in range(1,8):
    nascim = int(input(f"Em que ano nasceu a {hum}° pessoa?"))
    idade = atual - nascim
    if idade >= 21:
        totm += 1
    else:
        totmn += 1

print(f"{totm} pessoas são maiores")
print(f"{totmn} pessoas são menores")