from datetime import date
print("="*20)
print("    ALISTAMENTO")
print("="*20)

ano = int(input("Em que ano você nasceu? "))
idade = date.today().year - ano

if idade == 18:
    print(f"Você tem {idade} anos")
    print("Deve se alistar imediatamente")
elif idade < 18:
    print(f"Você tem {idade} anos")
    print(f"Ainda faltam {18-idade} para seu alistamento")
    print(f"Seu alistamento será em {ano+18}")
else:
    alis = str(input("Você ja se alistou? Dígite [s/n] ")).upper()
    if alis == 'S':
        print("Parabens se alistar é muito importante para o futuro!!!")
    else:
        print(f"Você tem {idade} anos")
        print(f"Você deveria ter se alistado a {idade-18} anos atrás")
        print(f"Seu alistamento foi em {ano+18}")

