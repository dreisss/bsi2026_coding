#!/usr/bin/env python

n1 = float(input("nota 1: "))
w1 = float(input("peso 1: "))

n2 = float(input("nota 2: "))
w2 = float(input("peso 2: "))

n3 = float(input("nota 3: "))
w3 = float(input("peso 3: "))

if 0 <= n1 <= 10 and 0 <= n2 <= 10 and 0 <= n3 <= 10:
    print(f"Média = {(n1 * w1 + n2 * w2 + n3 * w3) / (w1 + w2 + w3):.2f}")
else:
    print("Notas inválidas!")
