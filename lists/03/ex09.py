#!/usr/bin/env python

score = float(input("nota: "))

if 9 <= score <= 10:
    print("Conceito A")

elif 7 <= score < 9:
    print("Conceito B")

elif 5 <= score < 7:
    print("Conceito C")

elif 2.5 <= score < 5:
    print("Conceito D")

elif 0 <= score < 2.5:
    print("Conceito E")

else:
    print("Nota inválida!")
