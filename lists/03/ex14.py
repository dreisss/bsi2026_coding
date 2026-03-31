#!/usr/bin/env python

date = input("Digite uma data (dd/mm/aaaa): ")

day = int(date[0:2])
month = int(date[3:5])
year = int(date[6:10])

is_leap = False
month_max_date = 31

if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    is_leap = True

match month:
    case 4 | 6 | 9 | 11:
        month_max_date = 30

    case 2:
        if is_leap:
            month_max_date = 29
        else:
            month_max_date = 28

if 1 <= day <= month_max_date:
    print("Data válida")

    if is_leap:
        print("Ano bissexto")

else:
    print("Data inválida")
