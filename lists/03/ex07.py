#!/usr/bin/env python

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
d = int(input("Digite o valor de d: "))
e = int(input("Digite o valor de e: "))
f = int(input("Digite o valor de f: "))

det = a * e - b * d

if det == 0:
    print("Sistema sem solução")

else:
    x = (c * e - b * f) / det
    y = (a * f - c * d) / det

    print(f"x = {x:.4f}")
    print(f"y = {y:.4f}")
