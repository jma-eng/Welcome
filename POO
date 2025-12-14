# ----------------------------------------
# Programación Orientada a Objetos (POO)
# Promedio semanal del clima con colores
# ----------------------------------------

class Colores:
    """
    Clase auxiliar que define colores para la consola
    """
    AZUL = "\033[94m"
    VERDE = "\033[92m"
    AMARILLO = "\033[93m"
    ROJO = "\033[91m"
    RESET = "\033[0m"


class ClimaSemanal:
    """
    Clase que representa la información climática semanal
    """

    def __init__(self):
        # Encapsulamiento del atributo temperaturas
        self.temperaturas = []

    def ingresar_temperaturas(self):
        """
        Solicita al usuario las temperaturas de los 7 días
        """
        print(f"{Colores.AZUL}Ingreso de temperaturas semanales{Colores.RESET}")
        for dia in range(1, 8):
            temp = float(input(f"Día {dia}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Calcula y retorna el promedio semanal
        """
        return sum(self.temperaturas) / len(self.temperaturas)


def main():
    """
    Función principal del programa
    """
    print(f"{Colores.AMARILLO}Cálculo del promedio semanal del clima (POO){Colores.RESET}")

    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()

    print(f"{Colores.VERDE}El promedio semanal es: {promedio:.2f} °C{Colores.RESET}")


# Ejecución del programa
if __name__ == "__main__":
    main()
