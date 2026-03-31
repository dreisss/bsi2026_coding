#!/usr/bin/env python

a = float(input("valor de a: "))
b = float(input("valor de b: "))
c = float(input("valor de c: "))

if a + b < c or b + c < a or a + c < b:
    print("Essas medidas não formam um triângulo")

elif a == b == c:
    print("Triângulo Equilátero")

elif a == b or b == c or a == c:
    print("Triângulo Isósceles")

elif a != b and b != c and a != c:
    print("Triângulo Escaleno")
