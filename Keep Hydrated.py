import math

def litres(time):
    # Multiplicamos el tiempo por 0.5 y redondeamos hacia abajo
    litros = math.floor(time * 0.5)
    return f"Debe beber {litros} litros por las {time} horas."

# Ejemplos de uso
print(litres(3))
print(litres(6.7))
print(litres(11.8))