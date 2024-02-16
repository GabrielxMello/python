print("="*20)
print("   LOJA DO JEGUE")
print("="*20)

comp = float(input("Qual o valor da compra? R$"))
print("FORMA DE PAGAMENTO")
print("[1] Á vista dinheiro/cheque ")
print("[2] Á vista no cartão ")
print("[3] Em até 2x no cartão ")
print("[4] 3x ou mais no cartão ")
opção = int(input("Qual sua opção"))

if opção == 1:
    desc = comp * (10/100)
    print(f"Você ganhou um desconto de 10%, suas compras que custavam R${comp:.2f} passam a custar R${comp-desc:.2f}")
elif opção == 2:
    desc2 = comp * (5/100)
    print(f"Você ganhou um desconto de 5% suas compras que custavam R${comp:.2f} passam a custar R${comp-desc2:.2f}")
elif opção == 3:
    parcel = comp / 2
    print(f"Sua compra de R${comp:.2f} foi dividiva em duas parcelas de R${parcel:.2f} ")
else:
   parcelas = int(input("Quantas parcelas? "))
   juros = comp * (20/100)
   preço = comp + juros
   div = preço / parcelas
   print(f"Sua compra de R${comp:.2f} em {parcelas}x com juros, vai custar R${div:.2f} mensal custando R${preço:.2} no final")












