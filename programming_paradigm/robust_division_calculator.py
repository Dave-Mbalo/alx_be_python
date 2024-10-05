def conversion_attempt(value):

    try:

        float(value)
        return True
    
    except ValueError:

        return False


def safe_divide(numerator, denominator):
    
    if not conversion_attempt(numerator) or not conversion_attempt(denominator):
        return "Error: Please enter numeric values only."
    
    numerator = float(numerator)
    denominator = float(denominator)
    
    try:

        result = numerator / denominator
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:

        return "Error: Cannot devide by zero."
    



