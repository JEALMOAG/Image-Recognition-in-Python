from PIL import Image  # Importa la clase Image de la biblioteca PIL (Pillow)
import numpy as np     # Importa la biblioteca numpy bajo el alias np
import cv2             # Importa la biblioteca OpenCV bajo el alias cv2
import matplotlib.pyplot as plt  # Importa matplotlib.pyplot bajo el alias plt

# Abrir la imagen usando PIL
image = Image.open("puntos.png")

# Convertir la imagen a escala de grises
gray_image = image.convert('L')

# Convertir la imagen de PIL a un arreglo de NumPy
image_array = np.array(gray_image)

# Aplicar un umbral para binarizar la imagen
_, binary_image = cv2.threshold(image_array, 128, 255, cv2.THRESH_BINARY_INV)

# Encontrar los contornos de los objetos en la imagen binarizada
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Contar el número de contornos (objetos)
number_of_objects = len(contours)
print(f'Número de objetos en la imagen: {number_of_objects}')

# Visualizar los resultados
plt.figure(figsize=(12, 6))  # Crear una figura de tamaño 12x6 pulgadas

# Subtrama para la imagen original
plt.subplot(1, 2, 1)  # Crear una subtrama 1x2, mostrar en la posición 1
plt.title('Imagen Original')  # Establecer el título de la subtrama
plt.imshow(image, cmap='gray')  # Mostrar la imagen original en escala de grises
plt.axis('off')  # Desactivar los ejes en la subtrama

# Subtrama para la imagen con contornos
plt.subplot(1, 2, 2)  # Crear una subtrama 1x2, mostrar en la posición 2
plt.title('Imagen con Contornos')  # Establecer el título de la subtrama
contour_image = cv2.cvtColor(binary_image, cv2.COLOR_GRAY2BGR)  # Convertir imagen binaria a color BGR
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)  # Dibujar contornos en la imagen
plt.imshow(contour_image)  # Mostrar la imagen con contornos
plt.axis('off')  # Desactivar los ejes en la subtrama

plt.show()  # Mostrar la figura completa con ambas subtramas

