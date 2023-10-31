number = 1
count = 0
summ = 1
positive = False
while number <= 500:
    count += 1
    if positive:
        positive = False
    else:
        positive = True
    for i in range(count):
        number += 1
        if number > 500:
            break
        elif positive:
            summ += number
        else:
            summ -= number

print(summ)