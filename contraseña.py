# 🔐 Generador de contraseñas estilo red social segura

import random
import string

# Definimos los caracteres que se pueden usar
caracteres = string.ascii_letters + string.digits + string.punctuation

print("🔒 Bienvenido al generador de contraseñas ultra-seguras")
longitud = int(input("¿Qué tan larga quieres tu contraseña? (Ej: 12): "))

# Usamos comprensión de listas para formar la contraseña
contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))

print("✅ Tu nueva contraseña segura es:")
print(contrasena)
