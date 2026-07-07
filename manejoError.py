try:
    # Simulamos diferentes errores (descomenta uno por uno para probar)
    
    # 1. División por cero
    # resultado = 10 / 0

    # 2. Conversión inválida
    # numero = int("diez")

    # 3. Acceso a índice inexistente
    # lista = [1, 2, 3]
    # print(lista[5])

    # 4. Clave no encontrada en diccionario
    # diccionario = {"nombre": "Kai"}
    # print(diccionario["edad"])

    # 5. Archivo no encontrado
    # with open("archivo_inexistente.txt") as f:
    #     contenido = f.read()

    print("✅ El bloque try se ejecutó sin errores")

except ZeroDivisionError:
    print("❌ Error: No se puede dividir entre cero")

except ValueError:
    print("❌ Error: Valor inválido (por ejemplo, conversión incorrecta)")

except IndexError:
    print("❌ Error: Índice fuera del rango de la lista")

except KeyError:
    print("❌ Error: Clave no encontrada en el diccionario")

except FileNotFoundError:
    print("❌ Error: Archivo no encontrado")

except Exception as e:
    print("⚠️ Error desconocido:", type(e).__name__, "-", str(e))

finally:
    print("🔚 Bloque finally ejecutado: limpieza o cierre de recursos")