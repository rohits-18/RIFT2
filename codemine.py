import math

def divide_numbers(x: float, y: float) -> float:
    """
    This function divides two numbers.
    
    Args:
        x (float): The dividend.
        y (float): The divisor.
    
    Returns:
        float: The quotient of x and y.
    """
    if y == 0:
        return "Error: Division by zero is not allowed."
    else:
        return x / y

def main():
    x = 10
    y = 0
    print(divide_numbers(x, y))

if __name__ == "__main__":
    main()