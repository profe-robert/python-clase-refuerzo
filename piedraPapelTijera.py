# 🤖 Batalla digital: Piedra, papel o tijera contra la computadora

import random

opciones = ["piedra", "papel", "tijera"]

print("⚔️ Bienvenido al modo batalla: Piedra, Papel o Tijera")
print("Escribe 'salir' para terminar.\n")

# Repetimos hasta que el jugador escriba 'salir'
while True:
    jugador = input("Tu elección (piedra, papel, tijera): ").lower()

    if jugador == "salir":
        print("👋 ¡Gracias por jugar!")
        break

    if jugador not in opciones:
        print("❌ Opción inválida. Intenta de nuevo.")
        continue

    computadora = random.choice(opciones)
    print(f"🖥️ La computadora eligió: {computadora}")

    # Determinar resultado
    if jugador == computadora:
        print("🤝 ¡Empate!\n")
    elif (
        (jugador == "piedra" and computadora == "tijera") or
        (jugador == "papel" and computadora == "piedra") or
        (jugador == "tijera" and computadora == "papel")
    ):
        print("🏆 ¡Ganaste esta ronda!\n")
    else:
        print("😞 Perdiste esta ronda...\n")
