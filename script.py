# ----------------------------------------
# Programación Tradicional
# Cálculo del promedio semanal del clima
# ----------------------------------------

def ingresar_temperaturas():
    """
    Solicita al usuario las temperaturas de los 7 días de la semana.
    Retorna una lista con las temperaturas ingresadas.
    """
    temperaturas = []
    for dia in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas


def calcular_promedio(temperaturas):
    """
    Calcula el promedio semanal de las temperaturas.
    """
    return sum(temperaturas) / len(temperaturas)


def main():
    """
    Función principal del programa.
    """
    print("Cálculo del promedio semanal del clima")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")


# Ejecución del programa
if __name__ == "__main__":
    main()

