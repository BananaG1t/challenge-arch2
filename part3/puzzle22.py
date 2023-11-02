def find_largest_square(grid):
    max_sum = float('-1000') # just use any low number
    max_square = None

    for i in range(len(grid) - 2):  # 2 because we want a 3x3 square
        for j in range(len(grid[0]) - 2):  # 2 because we want a 3x3 square
            square_sum = 0
            square = []
            for x in range(i, i + 3):
                row = []
                for y in range(j, j + 3):
                    square_sum += grid[x][y]
                    row.append(grid[x][y])
                square.append(row)

            if square_sum > max_sum:
                max_sum = square_sum
                max_square = square

    return max_square, max_sum

# Define your grid here (16 rows and 15 columns)
grid = [
    [23, 92, 86, 40, 43, 88, 76, 86, 76, 20, 53, 26, 30, 55, 14],
    [74, 16, 58, 39, 72, 80, 16, 69, 39, 81, 27, 43, 19, 58, 15],
    [65, 46, 82, 92, 50, 59, 34, 18, 27, 42, 38, 80, 62, 73, 33],
    [77, 85, 69, 18, 58, 88, 39, 29, 24, 67, 29, 62, 41, 37, 77],
    [46, 95, 38, 19, 61, 40, 90, 70, 99, 16, 94, 51, 92, 62, 63],
    [43, 58, 90, 44, 49, 36, 51, 65, 25, 80, 52, 24, 94, 35, 93],
    [72, 24, 56, 42, 47, 77, 90, 61, 18, 36, 46, 39, 98, 11, 90],
    [73, 53, 61, 53, 31, 73, 23, 70, 41, 29, 36, 30, 24, 27, 30],
    [68, 47, 94, 31, 96, 42, 33, 62, 68, 63, 41, 72, 72, 68, 65],
    [48, 68, 92, 48, 94, 39, 84, 60, 35, 41, 87, 45, 89, 77, 67],
    [15, 87, 47, 68, 50, 37, 28, 51, 43, 98, 95, 91, 39, 29, 96],
    [60, 19, 37, 61, 36, 36, 81, 42, 56, 83, 29, 14, 27, 66, 15],
    [88, 78, 36, 50, 26, 70, 55, 38, 65, 94, 39, 92, 71, 73, 82],
    [96, 37, 87, 54, 22, 30, 49, 82, 15, 37, 55, 24, 14, 26, 72],
    [38, 85, 55, 44, 21, 71, 50, 83, 84, 84, 54, 99, 16, 92, 24],
    [17, 82, 51, 16, 70, 66, 69, 98, 40, 39, 49, 93, 24, 73, 77]
]

max_square, max_sum = find_largest_square(grid)

print("Largest 3x3 Square:")
for row in max_square:
    print(row)
print("Sum:", max_sum)
