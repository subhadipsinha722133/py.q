# 	WAP to demonstrate default arguments in a function (division of two numbers)
def divide_numbers(a, b=1):
    """
    Function to divide two numbers.
    
    Parameters:
        a (float): Dividend.
        b (float): Divisor. Default is 1.
    
    Returns:
        float: The result of dividing a by b.
    """
    return a / b

# Test cases
numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator (optional, press Enter for default value 1): ").strip() or 1)

result = divide_numbers(numerator, denominator)
print("Result of division:", result)
