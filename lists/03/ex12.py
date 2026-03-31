#!/usr/bin/env python

date = input("Digite uma data (dd/mm/aaaa): ")

months = [
    "janeiro",
    "fevereiro",
    "março",
    "april",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro",
]

day = date[0:2]
month = int(date[3:5])
year = date[6:10]

if 1 <= month <= 12:
    print(f"{day:02} de {months[month - 1]} de {year}")
else:
    print("Mês inválido!")
