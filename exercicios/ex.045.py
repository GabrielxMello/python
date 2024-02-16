from time import sleep
from random import choice

jokenpo = ['Pedra', 'Papel', 'Tesoura']
pc = choice(jokenpo)

print("="*25)
print("  Pedra, Papel e Tesoura")
print("="*25)
print("Suas opções:")
print("[0] Pedra")
print("[1] Papel")
print("[2] Tesoura")
escolha = int(input("Qual sua escolha? "))

print("=-" * 20)
print(f"Computador jogou {pc}")
print(f"Você jogou {jokenpo[escolha]}")
print("=-" * 20)

if escolha == 0 and pc == 'Tesoura':
    print("Você ganhou")
elif escolha == 0 and pc == 'Papel':
    print("Você perdeu")
elif escolha == 1 and pc == 'Pedra':
    print("Você ganhou")
elif escolha == 1 and pc == 'Tesoura':
    print("Você perdeu")
elif escolha == 2 and pc == 'Papel':
    print("Você ganhou")
elif escolha == 2 and pc == 'Pedra':
    print("Você perdeu")
else:
    print("empate")






