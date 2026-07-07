# Pedimos la edad al usuario
edad = int(input("¿Cuántos años tienes? "))

# Verificamos si cumple con la edad mínima
if edad >= 13:
    print("✅ Puedes crear una cuenta en Discord.")
else:
    print("❌ Lo siento, necesitas tener al menos 13 años.")
