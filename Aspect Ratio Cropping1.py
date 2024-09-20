'''
Programa que ajusta el recorte de relación de aspecto conservando la altura
'''
from PIL import Image
import math
def adjust_to_16_9(image_path, output_path):
    # Cargar la imagen
    with Image.open(image_path) as img:
        # Obtener dimensiones originales
        width, height = img.size

        # Calcula el nuevo ancho para mantener la altura y ajustar el aspecto 16:9
        new_width = height * (16 / 9)
        new_width_rounded = math.ceil(new_width)

        # Redimensionar la imagen a la nueva resolución
        new_size = (new_width_rounded, height)
        img_resized = img.resize(new_size, Image.Resampling.LANCZOS)

        # Guardar la imagen redimensionada
        img_resized.save(output_path)
        print(f"Imagen redimensionada y guardada en: {output_path}")

# Ruta a la imagen de entrada (reemplaza con la ruta a tu imagen)
input_image_path = r"C:\Users\reyna\Downloads\prueba.jpg"
# Ruta para guardar la imagen redimensionada (reemplaza con la ruta deseada)
output_image_path = r"C:\Users\reyna\Downloads\prueba_redimensionada.jpg"

# Llamar a la función con las rutas especificadas
adjust_to_16_9(input_image_path, output_image_path)