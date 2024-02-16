num = int(input("Dígite um número inteiro: "))
print("Escolha uma base para a conversão")
print("[1] Binário")
print("[2] Octal")
print("[3] Hexadecimal")
escol = int(input("Qual Opção deseja? "))
if escol == 1:
    bina = bin(num)
    print(f"O número {num} convertido para binário fica {bina[2:]}")
elif escol == 2:
    octa = oct(num)
    print(f"O número {num} convertudo para octal fica {octa[2:]}")
else:
    hexa = hex(num)
    print(f"O número {num} convertido para hexadecimal fica {hexa[2:]}")