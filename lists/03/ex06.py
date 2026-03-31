#!/usr/bin/env python

char = input("Digite um carctere: ")
result = ""

if char.isdecimal():
    result = "Dígito"

elif char.isalpha():
    result = "Letra maiúscula" if char.isupper() else "Letra minúscula"

elif char == " ":
    result = "Espaço em branco"

else:
    result = "Outro símbolo"

print(result)
