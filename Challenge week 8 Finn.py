#9 3 uur
unique_sets = set()  
for i in range(1, 10000):
    s = set([i * x * x % 1729 for x in range(1, 10000)])
    unique_sets.add(frozenset(s))  

print("Number of different sets:", len(unique_sets))




#35 6 uur 
# Dictionary with pizza names and their prices
pizzas = {
    'Americano': 13.45,
    'Beef': 15.80,
    'Calzone': 11.95,
    'Diet': 11.55,
    'Extra': 15.75,
    'Fantasia': 14.70
}

total_cost = 62  # Target total cost
istrue = False


for pizza in pizzas:
    if istrue:
        break
    for otherpizza2 in pizzas:
        if istrue:
            break
        for otherpizza3 in pizzas:
            if istrue:
                break
            for otherpizza4 in pizzas:
                combination = [pizza, otherpizza2, otherpizza3, otherpizza4]
                summ = pizzas[pizza] + pizzas[otherpizza2] + pizzas[otherpizza3] + pizzas[otherpizza4]
                if summ == 62:
                    istrue = True
                    break
if istrue:
    print(f"Combination found: {combination} (Total cost: {total_cost} euros)")
else:
    print("No combination found that sums up to 62 euros.")


#37 10 uur aangezeten en werkt niet
def message_to_code_dutch(message):
    dutch_values = {
        'A': '01', 'B': '02', 'C': '03', 'D': '04', 'E': '05', 'F': '06', 'G': '07', 'H': '08', 'I': '09',
        'J': '10', 'K': '20', 'L': '30', 'M': '40', 'N': '50', 'O': '60', 'P': '70', 'Q': '80', 'R': '90',
        'S': '21', 'T': '31', 'U': '41', 'V': '51', 'W': '61', 'X': '71', 'Y': '81', 'Z': '91'
    }

    code = ''
    for letter in message:
        if letter.upper() in dutch_values:
            code += dutch_values[letter.upper()]

    if len(code) < 5:
        code += '00' * ((5 - len(code)) // 2)  

    return code[:5]


encrypted_message = "TRIEHERTSUOSELCEHAOTHTESNRUIOEABWR" 
result = message_to_code_dutch(encrypted_message)
print(f"The 5-digit code for the encrypted message is: {result}")

#36 2 uur
import turtle
from turtle import Turtle

t = Turtle()

angle = 90
distances = [165, 215, 100, 530, 50, 225, 405, 235, 155, 245, 130, 140, 190, 165, 125, 155, 115, 235, 165, 140, 185, 200, 125, 195, 185, 125, 155, 215, 250, 215, 110, 180, 215, 165, 190, 180, 125, 120, 130, 215, 110, 130, 230, 150, 150, 100, 170, 150, 100, 245, 35]

for d in distances:
   t.forward(d)
   t.left(angle)

print(t.distance(0, 0))

turtle.done()

#veel aan opdrachten gezeten die uiteindelijk al werden opgelost door mijn teamgenoten. Heb deze codes niet opgeslagen (erg dom). Dit heeft voor mij de meeste werk gekost.
