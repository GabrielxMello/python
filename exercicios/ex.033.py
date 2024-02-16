num = int(input("Dígite um número: "))
num2 = int(input("Dígite outro número: "))
num3 = int(input("Dígite mais um número: "))

if num > num2 and num > num3:
    print(f"O maior número é {num}")
elif num2 > num  and num2 > num3:
    print(f"O maior numero é {num2}")
elif num3 > num and num3 > num2:
    print(f"O maior número é {num3}")
if num < num2 and num < num3:
    print(f"O menor número é {num}")
elif num2 < num and num2 < num3:
    print(f"O menor número é {num2}")
elif num3 < num2 and num3 < num:
    print(f"O menor número é {num3}")