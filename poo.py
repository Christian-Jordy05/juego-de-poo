from colorama import Fore, Style
import random

class Game:
    def __init__(self):
        self.secuencia = []
        self.intentoDeSecuencia = []
        self.azul = Fore.BLUE + " 🔵 " + Fore.RESET
        self.amarillo = Fore.YELLOW + " 🟡 " + Fore.RESET
        self.verde = Fore.GREEN + " 🟢 " + Fore.RESET
        self.rojo = Fore.RED + " 🔴 " + Fore.RESET

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
                print("┃ " + ' '.join(self.secuencia) + " ┃" + "  secuencia creada")
                print("")
            elif color == "G":
                numColo += 1
                self.secuencia.append(self.verde)
                print("┃ " + ' '.join(self.secuencia) + " ┃" + "  secuencia creada")
                print("")
            elif color == "Y":
                numColo += 1
                self.secuencia.append(self.amarillo)
                print("┃ " + ' '.join(self.secuencia) + " ┃" + "  secuencia creada")
                print("")
            elif color == "R":
                numColo += 1
                self.secuencia.append(self.rojo)
                print("┃ " + ' '.join(self.secuencia) + " ┃" + "  secuencia creada")
                print("")
                print("")

    def crearCompu(self):
        colores = [self.azul, self.amarillo, self.verde, self.rojo]
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
            verificadorDeColres = []
            for i in range(4):
                if intentoDeSecuencia[i] == self.secuencia[i]:
                    verificadorDeColres.append(Fore.GREEN + " 🟢 " + Fore.RESET)  
                elif intentoDeSecuencia[i] in self.secuencia:
                    verificadorDeColres.append(Fore.YELLOW + " 🟡 " + Fore.RESET) 
                else:
                    verificadorDeColres.append(Fore.RED + " 🔴 " + Fore.RESET)  
            print("Secuencia ingresada: " + ' '.join(intentoDeSecuencia))
            print("")
            print("verificador: " + ' '.join(verificadorDeColres))
            if intentoDeSecuencia == self.secuencia:
                print(Fore.GREEN + "¡Adivinaste la secuencia!" + Fore.RESET)
                break
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
            print("┃ " + ' '.join(h) + " ┃")
            print("┃                     ┃")
            if h == self.secuencia:
                print(Fore.GREEN + "¡La computadora adivinó la secuencia!" + Fore.RESET)
                break
            intentos += 1
        if intentos == 12:
            print(Fore.RED + "La computadora no pudo adivinar la secuencia." + Fore.RESET)

def main():
    juego = Game()
    # juego.bienvenida()
    juego.elegirModo()

main()