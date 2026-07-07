# 🐍 Clase de Refuerzo
Este repo contiene el material para una clase de refuerzo del contenido base de Python

## 1. Tipos de Variables
Las variables son "cajas" donde guardamos información. En Python no necesitas decir de qué tipo es, él lo adivina.

```python
# Enteros (números sin decimales)
edad = 25 

# Flotantes (números con decimales)
precio = 19.99 

# Cadenas de texto (String) - van entre comillas
nombre = "Ana" 

# Booleanos (Verdadero o Falso)
es_estudiante = True 
esta_aprobado = False

# Para saber el tipo de dato usamos type()
print(type(edad)) # Salida: <class 'int'>
```

## 2. Operadores Lógicos y Condicionales (`if`)
Evalúan condiciones para tomar decisiones.

*   `and`: Ambas condiciones deben ser verdaderas.
*   `or`: Al menos una condición debe ser verdadera.
*   `not`: Invierte el valor (de True a False o viceversa).

```python
edad = 20
tiene_entrada = True

# if (si), elif (sino si), else (sino)
if edad >= 18 and tiene_entrada:
    print("Puedes pasar a la fiesta.")
elif edad >= 18 and not tiene_entrada:
    print("Eres mayor, pero necesitas comprar entrada.")
else:
    print("Eres menor de edad, no puedes entrar.")
```

---

## 3. Estructura `case` (Match - Case)
*(Nota: Disponible desde Python 3.10 en adelante)*
Es una forma más limpia de evaluar múltiples opciones exactas (como un menú).

```python
dia_semana = "Martes"

match dia_semana:
    case "Lunes":
        print("Inicio de semana, ánimo.")
    case "Martes":
        print("Todavía falta para el viernes.")
    case "Viernes":
        print("¡Por fin es viernes!")
    case _:
        print("Es un día normal.") # El guion bajo (_) es el "por defecto"
```

---

## 4. Ciclos (Bucles)
Sirven para repetir acciones.

### Ciclo `for` (Repetir un número exacto de veces o recorrer elementos)
```python
# Repetir 5 veces (del 0 al 4)
for i in range(5):
    print(f"Iteración número: {i}")

# Recorrer una lista
frutas = ["manzana", "pera", "uva"]
for fruta in frutas:
    print(f"Me gusta comer {fruta}")
```

### Ciclo `while` (Repetir *mientras* una condición sea verdadera)
```python
contador = 3
while contador > 0:
    print(f"El contador vale: {contador}")
    contador = contador - 1 # ¡OJO: Siempre hay que cambiar la variable para no hacer un bucle infinito!
```

---

## 5. Listas y Diccionarios
Son estructuras para guardar múltiples datos a la vez.

### Listas
Son como filas de casilleros. Se accede a ellos por su posición (índice), empezando a contar desde 0.
```python
numeros = [10, 20, 30, 40, 50]

print(numeros[0])  # Salida: 10 (Primera posición)
print(numeros[-1]) # Salida: 50 (Última posición)

numeros.append(60) # Agrega un elemento al final
numeros.remove(20) # Elimina el elemento "20"
```

### Diccionarios
Son como cajas con etiquetas. Se accede a ellos por una "clave" (key), no por posición.
```python
persona = {
    "nombre": "Carlos",
    "edad": 35,
    "ciudad": "Madrid"
}

print(persona["nombre"]) # Salida: Carlos
persona["edad"] = 36     # Modificar un valor
persona["email"] = "c@c.com" # Agregar una nueva clave-valor
```

---

## 6. Funciones
Son bloques de código con un nombre que sirven para no repetir instrucciones. Se definen con `def`.

```python
# Crear la función (recibe dos parámetros)
def sumar(a, b):
    resultado = a + b
    return resultado # Devuelve el resultado

# Usar la función (llamarla)
mi_suma = sumar(5, 7)
print(f"El resultado de la suma es: {mi_suma}") # Salida: 12

# Función sin parámetros ni retorno
def saludar():
    print("¡Hola a todos!")

saludar()
```

---

## 7. Manejo de Excepciones (Try - Except)
Sirve para "atrapar" errores y que el programa no se detenga de forma brusca si algo falla (por ejemplo, dividir por cero o escribir letras donde van números).

```python
try:
    # Intentamos hacer algo que puede fallar
    numero = int(input("Escribe un número: "))
    division = 100 / numero
    print(f"El resultado es {division}")

except ZeroDivisionError:
    # Se ejecuta si específicamente hay división por cero
    print("Error: No puedes dividir entre cero.")

except ValueError:
    # Se ejecuta si el usuario escribe "Hola" en lugar de un número
    print("Error: Eso no es un número válido.")

except Exception as e:
    # Atrapa cualquier otro error inesperado
    print(f"Ocurrió un error desconocido: {e}")

finally:
    # Este bloque se ejecuta SIEMPRE, haya error o no
    print("Fin del programa.")
```

---

### 💡 Tips rápidos para la clase:
1. En Python **la indentación (los espacios al inicio)** es obligatoria y marca dónde empieza y termina un bloque de código (como lo que va dentro de un `if` o un `for`). Suele ser de 4 espacios.
2. Para imprimir texto y variables juntos, la forma más moderna y fácil es usar las **"f-strings"**: `print(f"Texto {variable}")`.
3. Los comentarios de una sola línea se hacen con el símbolo `#`.
```
