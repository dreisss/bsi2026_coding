min_salary = float(input("Salário mínimo (R$): "))
water = float(input("Água consumida (L): "))

bill = (water / 1000) * min_salary * (2 / 100)

print(f"Conta = R$ {bill:.2f}")
print(f"Conta com desconto = R$ {bill * (100 - 25.87) / 100:.2f}")
