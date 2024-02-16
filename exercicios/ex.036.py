casa = float(input("Qual o valor da casa? R$"))
sal = float(input("Qual o seu salário? R$"))
anos = int(input("Quantos anos para pagar a casa? "))
mensal = casa / (anos*12)
porcen = sal * (30/100)
if mensal > porcen:
    print(f"EMPRÉSTIMO NEGADO: Para pagar uma casa de R${casa:.2f} em {anos} anos, sua mensalidade "
          f"será de R${mensal:.2f}, com seu salário de R${sal:.2f} não consiguirá pagar valor.  " )
else:
    print(f"EMPRÉSTIMO APROVADO: Para pagar uma casa de R${casa:.2f} em {anos} anos, sua mensalidade "
          f"será de R${mensal:.2f}")

