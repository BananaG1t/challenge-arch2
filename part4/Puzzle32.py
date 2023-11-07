# Define grid as a list of lists
grid = [
    [24, 93, 87, 41, 44, 89, 77, 87, 77, 21, 54, 27, 31, 56, 15, 75, 17, 59, 40, 73, 81, 17, 70, 40, 82],
    [28, 44, 20, 59, 16, 66, 47, 83, 93, 51, 60, 35, 19, 28, 43, 39, 81, 63, 74, 34, 78, 86, 70, 19, 59],
    [89, 40, 30, 25, 68, 30, 63, 42, 38, 78, 47, 96, 39, 20, 62, 41, 91, 71, 17, 95, 52, 93, 63, 64, 44],
    [59, 91, 45, 50, 37, 52, 66, 26, 81, 53, 25, 95, 36, 94, 73, 25, 57, 43, 48, 78, 91, 62, 19, 37, 47],
    [40, 99, 12, 91, 74, 54, 62, 54, 32, 74, 24, 71, 42, 30, 37, 31, 25, 28, 31, 69, 48, 95, 32, 97, 43],
    [34, 63, 69, 64, 42, 73, 73, 69, 66, 49, 69, 93, 49, 95, 40, 85, 61, 36, 42, 88, 46, 90, 78, 68, 16],
    [88, 48, 69, 51, 38, 29, 52, 44, 99, 96, 92, 40, 30, 97, 61, 20, 38, 62, 37, 37, 82, 43, 57, 84, 30],
    [15, 28, 67, 16, 89, 79, 37, 51, 27, 71, 56, 39, 66, 95, 40, 93, 72, 74, 83, 97, 38, 88, 55, 23, 31],
    [50, 83, 16, 38, 56, 25, 15, 27, 73, 39, 86, 56, 45, 22, 72, 51, 84, 85, 85, 55, 17, 93, 25, 18, 83],
    [52, 17, 71, 67, 70, 99, 41, 40, 50, 94, 25, 74, 78, 17, 32, 61, 13, 43, 95, 12, 75, 50, 80, 85, 56],
    [83, 97, 12, 18, 79, 89, 61, 88, 76, 62, 21, 46, 20, 22, 38, 15, 49, 24, 93, 60, 21, 96, 92, 34, 69],
    [41, 32, 32, 26, 18, 91, 32, 54, 90, 24, 74, 71, 77, 19, 57, 98, 13, 19, 25, 24, 21, 20, 35, 80, 86],
    [96, 25, 27, 52, 48, 92, 79, 34, 51, 62, 80, 73, 86, 28, 38, 68, 48, 48, 47, 71, 43, 58, 82, 45, 90],
    [35, 18, 21, 67, 34, 33, 33, 57, 32, 30, 90, 25, 64, 83, 60, 72, 66, 88, 64, 31, 34, 53, 70, 35, 93],
    [53, 25, 82, 98, 18, 30, 46, 74, 74, 64, 43, 52, 81, 71, 79, 50, 95, 61, 64, 22, 13, 42, 67, 34, 14],
    [38, 38, 29, 85, 58, 66, 83, 18, 31, 65, 37, 94, 23, 30, 85, 44, 43, 47, 51, 46, 17, 18, 85, 37, 58],
    [96, 40, 90, 79, 95, 31, 41, 19, 87, 55, 97, 17, 95, 93, 15, 53, 36, 14, 41, 88, 21, 98, 14, 76, 75],
    [38, 78, 27, 43, 70, 96, 95, 85, 12, 44, 94, 69, 46, 51, 66, 86, 66, 54, 80, 57, 54, 39, 34, 54, 51],
    [35, 16, 20, 80, 59, 42, 83, 69, 17, 92, 41, 96, 93, 40, 85, 32, 83, 87, 14, 61, 97, 94, 36, 65, 86],
    [98, 46, 98, 77, 70, 81, 95, 32, 87, 17, 55, 97, 84, 60, 84, 53, 28, 62, 26, 89, 44, 61, 21, 31, 92],
    [17, 26, 20, 68, 13, 13, 80, 45, 57, 78, 17, 90, 55, 22, 70, 35, 89, 42, 15, 29, 66, 37, 36, 22, 85],
    [38, 55, 63, 80, 73, 66, 16, 51, 48, 65, 62, 65, 74, 40, 95, 87, 88, 59, 43, 79, 47, 54, 99, 46, 39],
    [89, 15, 51, 30, 33, 74, 33, 29, 48, 79, 64, 71, 12, 88, 59, 86, 72, 55, 46, 42, 79, 27, 39, 39, 91],
    [36, 15, 43, 92, 94, 35, 15, 85, 51, 94, 17, 66, 29, 40, 18, 86, 14, 14, 90, 45, 70, 24, 34, 51, 36],
    [96, 75, 39, 39, 35, 23, 32, 66, 66, 82, 58, 48, 96, 92, 22, 33, 83, 44, 26, 64, 20, 40, 56, 62, 74],
    [66, 70, 19, 70, 26, 95, 39, 17, 79, 87, 64, 99, 18, 25, 22, 15, 83, 67, 68, 55, 70, 73, 42, 62, 95],
    [37, 86, 93, 58, 34, 87, 52, 30, 29, 86, 26, 51, 84, 30, 89, 82, 30, 23, 61, 77, 25, 20, 82, 79, 40],
    [55, 84, 61, 85, 27, 65, 51, 16, 37, 45, 74, 64, 25, 19, 36, 32, 44, 72, 98, 84, 62, 36, 90, 75, 49],
    [43, 66, 23, 31, 63, 29, 90, 66, 22, 99, 87, 17, 96, 30, 17, 98, 79, 54, 44, 50, 75, 76, 52, 76, 14],
    [88, 73, 82, 48, 43, 49, 69, 66, 79, 88, 90, 17, 14, 62, 80, 83, 72, 24, 44, 17, 56, 14, 92, 27, 49],
    [21, 97, 83, 70, 47, 78, 91, 25, 65, 30, 70, 97, 71, 94, 80, 90, 63, 46, 16, 21, 91, 79, 27, 90, 72],
    [72, 85, 18, 28, 76, 82, 31, 92, 70, 52, 96, 74, 65, 40, 73, 22, 25, 73, 60, 31, 67, 12, 91, 87, 24],
    [23, 14, 29, 46, 32, 95, 76, 42, 45, 73, 71, 63, 24, 79, 39, 56, 29, 37, 32, 45, 19, 73, 60, 32, 87],
    [15, 15, 82, 34, 22, 73, 36, 65, 41, 50, 95, 16, 15, 23, 39, 37, 83, 93, 44, 47, 57, 25, 99, 68, 25],
    [59, 19, 84, 84, 22, 32, 17, 88, 21, 22, 57, 57, 29, 29, 45, 73, 67, 42, 75, 96, 15, 17, 87, 58, 18],
    [13, 70, 13, 77, 72, 95, 29, 41, 22, 99, 56, 41, 94, 92, 71, 25, 69, 50, 67, 71, 73, 85, 50, 89, 27],
    [15, 56, 30, 86, 62, 81, 50, 31, 68, 81, 32, 63, 40, 36, 72, 45, 15, 42, 74, 14, 29, 47, 56, 16, 24],
    [13, 53, 50, 75, 64, 78, 99, 54, 71, 14, 31, 53, 53, 90, 21, 67, 88, 75, 33, 19, 23, 27, 73, 12, 90],
    [37, 90, 60, 56, 61, 37, 27, 93, 21, 29, 82, 92, 73, 42, 28, 19, 40, 71, 57, 82, 83, 12, 79, 35, 25],
    [59, 59, 75, 84, 13, 55, 90, 14, 48, 45, 30, 25, 33, 63, 57, 80, 66, 88, 26, 81, 44, 27, 29, 13, 96]
]

# Initialize variables for the largest and smallest dips
largest_dip = None
smallest_dip = None

for row in range(len(grid)):
    for col in range(len(grid[0])):
        val = grid[row][col]
        is_dip = True
        
        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                if (r, c) != (row, col):
                    if r < 0 or r > 39 or c < 0 or c > 24:
                        is_dip = False
                    elif grid[r][c] <= val:
                        is_dip = False

        if is_dip:
            
            # Update the largest dip if it's the first or a larger dip is found
            if largest_dip is None or val > largest_dip:
                largest_dip = val
            # Update the smallest dip if it's the first or a smaller dip is found
            if smallest_dip is None or val < smallest_dip:
                smallest_dip = val
                    
if largest_dip is not None and smallest_dip is not None:
    # Calculate the product of the largest and smallest dips
    product_of_dips = largest_dip * smallest_dip
    print("Product of the largest dip and smallest dip:", product_of_dips)
else:
    print("No dips found in the grid.")