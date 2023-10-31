# The input string
input_string = "12345678987654321"

# keep track of the expressions
expressions = []

# Iterate through all possible combinations of evens
for i in range(len(input_string)):
    for j in range(i + 1, len(input_string)):
        expression = list(input_string)  # Make a copy of the string

        # Replace even positions with + and *
        expression[i] = '+'
        expression[j] = '*'

        # Make it into a string
        expr_str = "".join(expression)

        # Evaluate the expression
        try:
            result = eval(expr_str)

            # Check if the result ends with "132"
            if result % 1000 == 132:
                expressions.append((expr_str, result))
        except:
            pass

# Print the expressions and results
for expr, result in expressions:
    print(f"{expr} with value {result}")
