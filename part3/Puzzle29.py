for start in range(10000):
    sequence = [start]
    while sequence[-1] not in [1, 0]:
        if sequence[-1] % 2 == 0:
            sequence.append(int(sequence[-1] ** 0.5))
        else:
            sequence.append(int(sequence[-1] ** 1.5))
    if len(sequence) == 51:
        print(len(sequence))
        print(start)
        break