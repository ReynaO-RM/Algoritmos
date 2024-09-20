def mango(quantity, price_per_mango):
    # Calculate the number of sets of 3 mangoes
    sets_of_three = quantity // 3
    # Calculate the remaining mangoes after accounting for complete sets of 3
    remaining_mangoes = quantity % 3
    # Calculate the total number of mangoes to pay for
    mangoes_to_pay_for = (sets_of_three * 2) + remaining_mangoes
    # Calculate the total cost
    total_cost = mangoes_to_pay_for * price_per_mango
    #costo total teniendo en cuenta la oferta especial de "3 por 2".
    return f"El costo total de los mangos es de ${total_cost}."
# Ejemplos de uso:
print(mango(2, 3))
print(mango(3, 3))
print(mango(5, 3))
print(mango(9, 5))