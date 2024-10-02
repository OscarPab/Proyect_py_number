import random

def adivina_el_numero():
    # Genera un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    intentos = 0  # Contador de intentos

    print("¡Bienvenido al juego de Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100.")

    while True:
        # Solicita al usuario que ingrese un número
        intento = input("Introduce tu intento: ")

        # Verifica si la entrada es un número
        if not intento.isdigit():
            print("Por favor, introduce un número válido.")
            continue

        intento = int(intento)
        intentos += 1  # Incrementa el contador de intentos

        # Compara el intento del usuario con el número secreto
        if intento < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            # El usuario ha adivinado el número
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

# Llama a la función para iniciar el juego
adivina_el_numero()
