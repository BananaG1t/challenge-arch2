sum = 0
current_number = 1
series_length = 0

while series_length < 1000:
    current_number_str = str(current_number)
    
    for digit in current_number_str:
        sum += int(digit)
        series_length += 1
        
        if series_length >= 1000:
            break
    
    current_number += 1

print("Sum of 1st 1000:", sum)
