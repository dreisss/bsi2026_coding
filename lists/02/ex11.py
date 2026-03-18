d = int(input("Idade (dias): "))

y = d // 365
m = (d % 365) // 30
d = (d % 365) % 30

print(f"{y} ano(s) {m} mes(es) e {d} dia(s)")
