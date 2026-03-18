t = float(input("Tempo (seg): "))

d1 = (299792458 * t) / 1000
d2 = (343.20 * t) / 1000

print(f"Distância percorrida pela luz em {t:.2f} seg é {d1:.2f} km")
print(f"Distância percorrida pelo som em {t:.2f} seg é {d2:.2f} km")
