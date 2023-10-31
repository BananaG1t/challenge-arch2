"""
Alice, Bob, Chris and Diana are participating in the New York Marathon.
Alice (a nerd) remarks: “look, all our registration numbers are perfect squares!”.
Bob (even more nerdish): “And when you increase the numbers with 105, it will be squares again!”.
Chris (a prime nerd): “My number has 2 different prime divisors”.
What is the registration number of Chris?
"""


from math import sqrt


primenumbs = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
              43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

for number in range(10000001):
    if sqrt(number).is_integer():
        if sqrt(number + 105).is_integer():
            times = 0
            two = False
            for prime in primenumbs:
                if number % prime == 0:
                    times += 1
                if times == 2 and not two:
                    print(number)
                    two = True
                if times > 2:
                    print(f"{number} has too many")
