'''
Programa que calcula la presión total
'''
def calculate_total_pressure(M1, M2, m1, m2, V, T_C):
    # Convert temperature from Celsius to Kelvin
    T_K = T_C + 273.15

    # Gas constant in dm³·atm·K⁻¹·mol⁻¹
    R = 0.082

    # Calculate the total pressure
    P_total = ((m1 / M1) + (m2 / M2)) * R * T_K / V

    return P_total

# Example usage:
M1 = 32.00  # masa molar de gas 1 en g/mol (por ejemplo, oxígeno)
M2 = 44.01  # masa molar del gas 2 en g/mol (por ejemplo, dióxido de carbono)
m1 = 5.00  # masa de gas 1 en gramos
m2 = 10.00  # masa de gas 2 en gramos
V = 10.00  # volumen del recipiente en dm³
T_C = 25.00  # temperatura en grados Celsius

P_total = calculate_total_pressure(M1, M2, m1, m2, V, T_C)
print(f"La presión total ejercida por los gases es: {P_total:.2f} atm")