'''
Programa que calcula la edad de un perro y un gato con respecto a los años humanos
'''
def calculate_pet_ages(human_years):
    # Inicializamos las variables para los años de los gatos y los perros
    cat_years = 0
    dog_years = 0
    # Calculamos los años de los gatos
    if human_years == 1:
        cat_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4
    # Calculamos los años de los perros
    if human_years == 1:
        dog_years = 15
    elif human_years == 2:
        dog_years = 15 + 9
    else:
        dog_years = 15 + 9 + (human_years - 2) * 5
    #return [human_years, cat_years, dog_years]
    return {
        'Años humanos': human_years,
        'Años gatos': cat_years,
        'Años perros': dog_years
    }
human_years = 5
result = calculate_pet_ages(human_years)
print(result)
print(type(result))