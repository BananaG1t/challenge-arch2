"""
Alice, Bob, Chris and Diana are participating in the New York Marathon.
Alice (a nerd) remarks: “look, all our registration numbers are perfect squares!”.
Bob (even more nerdish): “And when you increase the numbers with 105, it will be squares again!”.
Chris (a prime nerd): “My number has 2 different prime divisors”.
What is the registration number of Chris?
"""


from math import sqrt


for i in range(1001):
    if sqrt(i).is_integer():
        if sqrt(i + 105).is_integer():
            print(i + 105)