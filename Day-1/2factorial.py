def factorial(n):
    """Returns the factorial of a given number n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def main():
    # Example usage of the factorial function
    try:
        number = int(input("Enter a non-negative integer: "))
        result = factorial(number)
        print(f"The factorial of {number} is {result}.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()