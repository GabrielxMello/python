frase = str(input("Escreva uma frase: ")).upper().strip()
print(f"A letra a aparece {frase.count("A")} vezes na frase")
print(f"O primeiro A aparece na posição {frase.find('A')+1}")
print(f"A última letra A aparece na posição {frase.rfind('A')+1}")


