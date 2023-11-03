
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