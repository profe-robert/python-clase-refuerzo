# 📋 Encuesta estilo comunidad gamer

print("🎮 ¡Bienvenido a la encuesta de videojuegos favoritos!")
print("Escribe 'salir' cuando termines.\n")

respuestas = []  # Lista para guardar los juegos favoritos

while True:
    juego = input("¿Qué juego te ha gustado más este año?: ")
    if juego.lower() == "salir":
        break
    respuestas.append(juego)  # Agregamos cada respuesta a la lista

# Mostramos el resumen de la comunidad
print("\n📊 Resultados de la encuesta gamer:")
for i, respuesta in enumerate(respuestas, start=1):
    print(f"{i}. {respuesta}")
