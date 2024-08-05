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
        self.secuencia = random.choices(colores, k=4)
        print(Fore.GREEN + "¡Secuencia creada por la computadora!" + Fore.RESET)
        print(' '.join(self.secuencia))

    def adivinaJugador(self):
        
        print("El jugador crea una secuencia.")
        self.crearCompu()
        intentos = 0
        while intentos < 12:
            intento = input("Ingresa tu secuencia de colores: ").upper().split()
            intentoDeSecuencia = [self.azul if color == "B" else self.amarillo if color == "Y" else self.verde if color == "G" else self.rojo for color in intento]
            aciertos_posicion = sum(1 for i in range(4) if intentoDeSecuencia[i] == self.secuencia[i])
            aciertos_color = sum(min(intentoDeSecuencia.count(color), self.secuencia.count(color)) for color in [self.azul, self.amarillo, self.verde, self.rojo]) - aciertos_posicion
            if intentoDeSecuencia == self.secuencia:
                print(Fore.GREEN + "¡Adivinaste la secuencia!" + Fore.RESET)
                break
            else:
                print(Fore.RED + f"Secuencia incorrecta. Tienes {aciertos_posicion} colores en la posición correcta y {aciertos_color} colores correctos en la posición incorrecta. Inténtalo de nuevo." + Fore.RESET)
            intentos += 1
        if intentos == 12:
            print(Fore.RED + "Se acabaron los intentos. La secuencia era: " + ' '.join(self.secuencia) + Fore.RESET)

    def adivinaComputadora(self):
        print("El jugador crea una secuencia.")
        self.crearJugador()
        colores = [self.azul, self.amarillo, self.verde, self.rojo]
        intentos = 0
        while intentos < 12:
            h = random.choices(colores, k=4)
            print("La computadora intenta: " + ' '.join(h))
            if h == self.secuencia:
                print(Fore.GREEN + "¡La computadora adivinó la secuencia!" + Fore.RESET)
                break
            intentos += 1
        if intentos == 12:
            print(Fore.RED + "La computadora no pudo adivinar la secuencia." + Fore.RESET)

def main():
    juego = Game()
    juego.bienvenida()
    juego.elegirModo()


main()