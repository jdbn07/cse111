import random
def roll_dice(num_dice, num_sides):
    """Simula el lanzamiento de un dado.

    Parameters:
        num_dice (int): El número de dados a lanzar.
        num_sides (int): El número de caras en cada dado.

    Returns:
        list: Una lista de los resultados de los lanzamientos.
    """
    return [random.randint(1, num_sides) for _ in range(num_dice)]

def main():
    print("Bienvenido al simulador de lanzamiento de dados.")

    while True:
        num_dice = int(input("Ingrese el número de dados a lanzar: "))
        num_sides = int(input("Ingrese el número de caras en cada dado: "))

        if num_dice <= 0 or num_sides <= 0:
            print("Por favor, ingrese números enteros positivos.")
            continue

        # Simular el lanzamiento de los dados
        results = roll_dice(num_dice, num_sides)

        # Mostrar los resultados
        print("Resultados del lanzamiento:", results)

        # Preguntar al usuario si desea lanzar los dados nuevamente
        play_again = input("¿Desea lanzar los dados nuevamente? (s/n): ").lower()
        if play_again != 's':
            break

    print("Gracias por usar el simulador de lanzamiento de dados. ¡Hasta luego!")

if __name__ == "__main__":
    main()