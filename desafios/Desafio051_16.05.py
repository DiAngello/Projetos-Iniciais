a1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))
for c in range(1, 11):
    an = a1 + (c - 1) * r
    print(an)
