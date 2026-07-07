# ==========================================
# 1. DEFINICIÓN DE VARIABLES Y DICCIONARIOS
# ==========================================
# Usamos diccionarios para agrupar las estadísticas de cada personaje.
# Esto es mucho más ordenado que crear variables sueltas (nombre1, hp1, etc).

jugador_1 = {
    "nombre": "Caballero",
    "hp": 100,        # Puntos de vida (Health Points)
    "ataque": 15,
    "defensa": 8
}

jugador_2 = {
    "nombre": "Mago Oscuro",
    "hp": 80,
    "ataque": 25,
    "defensa": 4
}

# Variable de control para el bucle principal del menú
activa = True 

# ==========================================
# 2. CICLO PRINCIPAL (MENÚ)
# ==========================================
# Usamos un ciclo while infinito (while True o mientras activa sea True).
# Solo saldremos de aquí cuando el usuario elija la opción "Salir".

while activa:
    print("\n" + "="*40)
    print("   SIMULADOR DE BATALLA RPG")
    print("="*40)
    print("1. Iniciar Batalla")
    print("2. Ver Estadísticas")
    print("3. Editar Personajes")
    print("4. Salir")
    print("="*40)
    
    # Pedimos la opción al usuario
    opcion = input("Elige una opción (1-4): ")
    
    # ------------------------------------------
    # CONDICIONALES (IF / ELIF / ELSE) DEL MENÚ
    # ------------------------------------------
    
    if opcion == "1":
        print(f"\n¡Comienza la batalla entre {jugador_1['nombre']} y {jugador_2['nombre']}!")
        
        # IMPORTANTE: Hacemos una copia de los diccionarios usando .copy()
        # Si no hacemos esto, el daño se aplicaría a los datos originales
        # y si volvemos a pelear, empezarían con 0 de vida.
        p1 = jugador_1.copy()
        p2 = jugador_2.copy()
        
        # ------------------------------------------
        # CICLO DE BATALLA (WHILE)
        # ------------------------------------------
        # La batalla se repite MIENTRAS ambos tengan vida (hp > 0)
        while p1["hp"] > 0 and p2["hp"] > 0:
            input("\nPresiona ENTER para el siguiente turno...") # Pausa dramática
            
            # --- TURNO DEL JUGADOR 1 ATACA A JUGADOR 2 ---
            # Fórmula de daño simple: Atacante - Defensor. Mínimo 1 de daño.
            daño_p1 = p1["ataque"] - p2["defensa"]
            if daño_p1 < 1:
                daño_p1 = 1 # La defensa nunca puede curar, el mínimo es 1
                
            p2["hp"] = p2["hp"] - daño_p1 # Restamos la vida al defensor
            print(f"⚔️ {p1['nombre']} ataca a {p2['nombre']} y le hace {daño_p1} de daño. (HP restante: {p2['hp']})")
            
            # Comprobamos si el jugador 2 murió antes de que este contraataque
            if p2["hp"] <= 0:
                break # Rompe el ciclo de batalla inmediatamente
                
            # --- TURNO DEL JUGADOR 2 ATACA A JUGADOR 1 ---
            daño_p2 = p2["ataque"] - p1["defensa"]
            if daño_p2 < 1:
                daño_p2 = 1
                
            p1["hp"] = p1["hp"] - daño_p2
            print(f"🔥 {p2['nombre']} ataca a {p1['nombre']} y le hace {daño_p2} de daño. (HP restante: {p1['hp']})")
            
        # ------------------------------------------
        # FIN DE LA BATALLA
        # ------------------------------------------
        print("\n--- BATALLA TERMINADA ---")
        if p1["hp"] > 0:
            print(f"🏆 ¡{p1['nombre']} ha ganado la batalla!")
        else:
            print(f"🏆 ¡{p2['nombre']} ha ganado la batalla!")
            
    elif opcion == "2":
        # Mostramos los valores accediendo a las claves del diccionario
        print("\n--- ESTADÍSTICAS ACTUALES ---")
        print(f"Jugador 1: {jugador_1}")
        print(f"Jugador 2: {jugador_2}")
        
    elif opcion == "3":
        print("\n--- EDITAR PERSONAJES ---")
        print("¿A quién quieres editar?")
        print("1. " + jugador_1["nombre"])
        print("2. " + jugador_2["nombre"])
        
        # ------------------------------------------
        # MANEJO DE EXCEPCIONES (TRY - EXCEPT)
        # ------------------------------------------
        # Usamos try porque el usuario podría escribir letras en lugar del número 1 o 2
        try:
            quien_editar = int(input("Elige (1 o 2): "))
            
            # Validamos que sea 1 o 2
            if quien_editar == 1 or quien_editar == 2:
                
                # Seleccionamos el diccionario temporalmente
                objetivo = jugador_1 if quien_editar == 1 else jugador_2
                
                print(f"\nEditando a: {objetivo['nombre']}")
                print("1. Nombre")
                print("2. HP")
                print("3. Ataque")
                print("4. Defensa")
                
                stat = input("¿Qué stat quieres cambiar? (1-4): ")
                
                # Pedimos el nuevo valor
                nuevo_valor = input("Introduce el nuevo valor: ")
                
                # Si cambiamos el HP, Ataque o Defensa, deben ser números enteros (int)
                # Aquí usamos OTRO try-except anidado por si intenta poner "Hola" en el Ataque
                if stat in ["2", "3", "4"]:
                    try:
                        nuevo_valor = int(nuevo_valor) # Intentamos convertir texto a número
                        # Actualizamos el diccionario según la opción
                        if stat == "2": objetivo["hp"] = nuevo_valor
                        if stat == "3": objetivo["ataque"] = nuevo_valor
                        if stat == "4": objetivo["defensa"] = nuevo_valor
                        print("✅ Stat actualizado correctamente.")
                    except ValueError:
                        print("❌ Error: Para HP, Ataque y Defensa debes escribir un número.")
                elif stat == "1":
                    objetivo["nombre"] = nuevo_valor # El nombre sí puede ser texto
                    print("✅ Nombre actualizado correctamente.")
                else:
                    print("❌ Opción de stat no válida.")
            else:
                print("❌ Opción no válida. Debes elegir 1 o 2.")
                
        except ValueError:
            # Si falla el primer int(input()), cae aquí
            print("❌ Error: Eso no era un número válido. Vuelve al menú.")
            
    elif opcion == "4":
        print("\n¡Saliendo del simulador! ¡Hasta la próxima!")
        activa = False # Cambiamos la variable a False para que el ciclo while termine
        
    else:
        # Si escribe un 5, o una letra en el menú principal
        print("❌ Opción no reconocida. Intenta de nuevo.")