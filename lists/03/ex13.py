#!/usr/bin/env python

from math import sqrt

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4 * a * c

print(f"delta = {delta:.4f}")

if delta == 0:
    print(f"x = {-b / (2 * a):.4f}")

elif delta > 0:
    print(f"x1 = {(-b + sqrt(delta)) / (2 * a):.4f}")
    print(f"x2 = {(-b - sqrt(delta)) / (2 * a):.4f}")

elif delta < 0:
    print("Não há raízes")
