# 📚 Este programa simula una calculadora básica con funciones.

# Función para sumar dos números
def sumar(a, b):
    return a + b

# Función para restar dos números
def restar(a, b):
    return a - b

# Función para multiplicar dos números
def multiplicar(a, b):
    return a * b

# Función para dividir dos números
def dividir(a, b):
    if b == 0:
        return "No se puede dividir por cero"
    return a / b

# Menú con estilo gamer
print("🎮 Calculadora Gamer: Elige tu ataque matemático")
print("1. Sumar 🧠")
print("2. Restar 💥")
print("3. Multiplicar 🔥")
print("4. Dividir ⚔️")

opcion = input("Selecciona una opción (1-4): ")

# Entrada de datos
num1 = float(input("Ingresa tu primer número: "))
num2 = float(input("Ingresa tu segundo número: "))

# Evaluamos la opción y usamos las funciones
if opcion == "1":
    print("Resultado:", sumar(num1, num2))
elif opcion == "2":
    print("Resultado:", restar(num1, num2))
elif opcion == "3":
    print("Resultado:", multiplicar(num1, num2))
elif opcion == "4":
    print("Resultado:", dividir(num1, num2))
else:
    print("⚠️ Opción no válida")
