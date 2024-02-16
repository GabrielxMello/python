prod = float(input("Qual o preço do produto? R$"))
desc = prod * (5/100)
print(f"O produto que custava R${prod:.2f}, com o desconto de 5% passa a custar R${prod-desc:.2f}")