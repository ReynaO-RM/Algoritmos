'''
Programa que calcula el rendimiento del jugador en base a su tiempo de juego actual
'''
def nba_extrap(ppg, mpg):
    # Handle edge case where MPG is 0
    if mpg == 0:
        return "El rendimiento del jugador en base a su tiempo de juego actual es: 0"

    # Calculate Points Per Minute (PPM)
    ppm = ppg / mpg

    # Extrapolate to 48 minutes
    extrapolated_ppg = ppm * 48

    # Round to the nearest tenth
    rounded_ppg = round(extrapolated_ppg, 1)

    return f"El rendimiento del jugador en base a su tiempo de juego actual es: {rounded_ppg}"


# Ejemplos de uso:
print(nba_extrap(12, 20))
print(nba_extrap(10, 10))
print(nba_extrap(5, 17))
print(nba_extrap(0, 0))