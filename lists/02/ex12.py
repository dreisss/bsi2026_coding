t = int(input("Tempo (seg): "))

h = t // (60 * 60)
m = (t % (60 * 60)) // 60
s = (t % (60 * 60)) % 60

print(f"{h:02d}:{m:02d}:{s:02d}")
