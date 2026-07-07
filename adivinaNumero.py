# 👾 Juego: Adivina el número secreto que oculta el sistema

import random  # Importamos librería para generar números aleatorios

numero_secreto = random.randint(1, 50)  # Número aleatorio entre 1 y 50
intentos = 0

print("🎯 ADIVINA EL NÚMERO (modo hacker)")
print("Estoy pensando en un número entre 1 y 50... ¿Cuál será?")

# Ciclo hasta que el jugador adivine
while True:
    intento = int(input("Haz tu intento: "))
    intentos += 1

    if intento < numero_secreto:
        print("Muy bajo... intenta con un número mayor.")
    elif intento > numero_secreto:
        print("Muy alto... intenta con un número menor.")
    else:
        print(f"¡Correcto! Adivinaste en {intentos} intentos.")
        break
