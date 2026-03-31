#!/usr/bin/env python

age = int(input("Digite a idade: "))

is_donor = 18 <= age <= 67

print("Doador" if is_donor else "Não doador")
