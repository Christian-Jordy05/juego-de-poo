from colorama import Fore
import random
class Game:
    def _init_(self): 
        self.secuencia = []
        self.intentoDeSecuencia = []

    def bienvenida(self):
        print(Fore.GREEN + "Bienvenido usuario, ¿listo para jugar?" + Fore.RESET)
        veri = input("S/N: ").lower()
        if veri == "s":
            print(Fore.GREEN + "Okey, pero antes de empezar el juego, ¿me puedes decir tu nombre?" + Fore.RESET)
            nombreDeUser = input("Dime tu nombre: ")
            print(f"Hola {Fore.BLUE}{nombreDeUser}{Fore.RESET}, el juego ya va a empezar.")
        else:
            print(Fore.RED + "Adiós usuario, que tengas un excelente día." + Fore.RESET)
            exit()

    def elegirModo(self):
        while True:
            print(Fore.GREEN + 'Adivinas o creas la secuencia. (Adivinar / Crear)' + Fore.RESET)
            respuesta = input("R/: ").strip().lower()
            if respuesta not in ('adivinar', 'crear'):
                print("Por favor, agrega una respuesta correcta.")
            else:
                if respuesta == 'adivinar':
                    self.adivinaComputadora()
                elif respuesta == 'crear':
                    self.adivinaJugador()
                break

    def crearJugador(self):
        colores = ['verde', 'azul', 'amarillo', 'rojo']

    def crearCompu(self):
        azul = Fore.BLUE + "O" 
        amarillo = Fore.YELLOW + "O" 
        verde = Fore.GREEN + "O" 
        rojo = Fore.RED + "O" 
        colores = [azul, amarillo, verde, rojo]
        self.secuencia = random.choices(colores, k=4)
        print(Fore.GREEN + "¡Secuencia creada por la computadora!" + Fore.RESET)
        print(' '.join(self.secuencia))

    def adivinaJugador(self):
        print("El jugador crea una secuencia.")
        self.crearJugador()

    def adivinaComputadora(self):
        print("La computadora crea una secuencia.")
        self.crearCompu()

def main():
    juego = Game()
    juego.bienvenida()
    juego.elegirModo()

main()