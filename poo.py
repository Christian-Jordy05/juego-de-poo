from colorama import Fore, Style
import random

class Game:
    def __init__(self): 
        self.secuencia = []
        self.intentoDeSecuencia = []
        self.azul = Fore.BLUE + "O" + Fore.RESET
        self.amarillo = Fore.YELLOW + "O" + Fore.RESET
        self.verde = Fore.GREEN + "O" + Fore.RESET
        self.rojo = Fore.RED + "O" + Fore.RESET
        
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
                    self.adivinaJugador()
                elif respuesta == 'crear':
                    self.adivinaComputadora()
                break

    def crearJugador(self):
        numColo = 0
        while numColo < 4:
            print(Fore.GREEN + "Colores: " + Fore.BLUE + "azul = B, " + Fore.YELLOW + "amarillo = Y, " + Fore.RED + "rojo = R, " + Fore.GREEN + "verde = G" + Fore.RESET)
            color = input("Ingresa el orden de los colores: ").upper()
            if color == "B":
                numColo += 1
                self.secuencia.append(self.azul)
                print(' '.join(self.secuencia))
            elif color == "G":
                numColo += 1
                self.secuencia.append(self.verde)
                print(' '.join(self.secuencia))
            elif color == "Y":
                numColo+= 1
                self.secuencia.append(self.amarillo )
                print(' '.join(self.secuencia))
            elif color == "R":
                numColo += 1
                self.secuencia.append(self.rojo)
                print(' '.join(self.secuencia))

    def crearCompu(self):
        colores = [self.azul, self.amarillo , self.verde, self.rojo]
 

    def adivinaJugador(self):
        
        print("El jugador crea una secuencia.")
        self.crearCompu()

    def adivinaComputadora(self):
        print("El jugador crea una secuencia.")
        self.crearJugador()

def main():
    juego = Game()
    juego.bienvenida()
    juego.elegirModo()


main()