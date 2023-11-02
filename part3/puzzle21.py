def recaman_sequence(n):
    sequence = [0]  # Initialize with the first term, a(0) = 0
    seen = set(sequence)  # Keep track of numbers already in the sequence

    for i in range(1, n):
        previous_term = sequence[i - 1]
        next_term = previous_term - i

        # If the next term is non-negative and not already in the sequence, add it
        if next_term > 0 and next_term not in seen:
            sequence.append(next_term)
            seen.add(next_term)
        else:
            next_term = previous_term + i
            sequence.append(next_term)
            seen.add(next_term)

    return sequence

n = 1000
recaman_sequence_1000 = recaman_sequence(n)
print(recaman_sequence_1000[-1])
