def usd_to_cny(usd):
    # Tasa de conversión
    conversion_rate = 6.75
    # Convertir USD a CNY
    cny = usd * conversion_rate
    # Formatear el resultado a 2 decimales y retornar como cadena con 'Chinese Yuan'
    return f"{usd} usd equivalen a {cny:.2f} Chinese Yuan"

# Ejemplos de uso
print(usd_to_cny(15))
print(usd_to_cny(465))