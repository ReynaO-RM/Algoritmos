def round_to_two_decimal_places(number):
    # Round the number to two decimal places
    rounded_number = round(number, 2)

    # Return the rounded number as a string with two decimal places
    return f"De {number} el número redondeado es: {rounded_number:.2f}"


# Ejemplos de uso:
print(round_to_two_decimal_places(5.5589))  # '5.56'
print(round_to_two_decimal_places(3.3424))  # '3.34'
print(round_to_two_decimal_places(1.1))  # '1.10'
print(round_to_two_decimal_places(7.777))  # '7.78'