'''
Programa que calcula el tercer ángulo de un triángulo
'''
def third_angle(angle1, angle2):
    # La suma de los ángulos de un triángulo es 180 grados
    third = 180 - (angle1 + angle2)
    # Devolvemos el tercer ángulo junto con un mensaje explicativo
    return f"El tercer ángulo es {third} grados."

# Ejemplos de uso
print(third_angle(60, 60))
print(third_angle(45, 90))