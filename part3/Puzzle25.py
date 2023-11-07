guesses = [35, 146, 1736]

for x in range(10000000):
    a = x - 35
    b = x - 146
    c = x - 1736
    if a < 0:
        a = a * -1
    if b < 0:
        b = b * -1
    if c < 0:
        c = c * -1
    if (a*b*c) == 606029204:
        print(x)
        break