puzzle = "abacabaaabcc"

for a in range(8):
    for b in range(8):
        for c in range(8):
            newone = puzzle.replace("a", str(a))
            newtwo = newone.replace("b", str(b))
            newthree = newtwo.replace("c", str(c))
            number = str(int(newthree, 8))
            lenght = len(number)
            if lenght >= 3:
                if number[lenght-3:lenght] == "736":
                    print(number)