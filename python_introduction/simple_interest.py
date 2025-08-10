def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest using the formula:
    SI = (P * R * T) / 100

    Parameters:
    principal (float): The principal amount
    rate (float): The annual interest rate
    time (float): The time in years

    Returns:
    float: The calculated simple interest
    """
    return (principal * rate * time) / 100

# Example usage
print("Simple Interest for P=1000, R=5%, T=3 years is:", calculate_simple_interest(1000, 5, 3))