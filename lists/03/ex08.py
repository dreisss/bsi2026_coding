#!/usr/bin/env python

year = int(input("Digite o ano do casamento: "))
age = 2026 - year
result = ""

match age:
    case 5:
        result = "Bodas de Ferro"

    case 10:
        result = "Bodas de Estanho"

    case 20:
        result = "Bodas de Porcelana"

    case 25:
        result = "Bodas de Prata"

    case 50:
        result = "Bodas de Ouro"

    case 60:
        result = "Bodas de Diamante"

    case 70:
        result = "Bodas de Vinho"

    case 80:
        result = "Bodas de Carvalho"

    case _:
        result = f"Casados há {age} anos"


print(result)
