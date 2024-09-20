'''
Programa que calcula el rango mínimo y máximo de edad para la compatibilidad
'''
import math

def age_range(age):
    if age <= 14:
        # Calculate the min and max age for ages 14 or less
        min_age = math.floor(age - 0.10 * age)
        max_age = math.floor(age + 0.10 * age)
    else:
        # Calculate the min and max age for ages greater than 14
        min_age = math.floor(age / 2 + 7)
        max_age = math.floor(2 * (age - 7))

    return (f" Para la edad de {age} años el rango "
            f"mínimo es de {min_age} y el máximo de {max_age}")

# Ejemplos de uso:
print(age_range(27))  # '20-40'
print(age_range(5))  # '4-5'
print(age_range(17))  # '15-20'