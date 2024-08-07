from colorama import Fore
import random
import time

class Game:
    def __init__(self):
        self.secuencia = []
        self.azul = Fore.BLUE + " 🔵 " + Fore.RESET
        self.amarillo = Fore.YELLOW + " 🟡 " + Fore.RESET
        self.verde = Fore.GREEN + " 🟢 " + Fore.RESET
        self.rojo = Fore.RED + " 🔴 " + Fore.RESET
        self.colores = [self.azul, self.amarillo, self.verde, self.rojo]
        self.tabla = [["⚪" for _ in range(4)] for _ in range(12)] 
        self.verificadores = [["⚪" for _ in range(4)] for _ in range(12)]  
        self.historial = [] 

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
                    self.elegirDificultad()
                break

    def elegirDificultad(self):
        while True:
            print(Fore.GREEN + 'Elige la dificultad para la computadora. (Fácil / Difícil)' + Fore.RESET)
            dificultad = input("R/: ").strip().lower()
            if dificultad not in ('fácil', 'facil', 'difícil', 'dificil'):
                print("Por favor, agrega una respuesta correcta.")
            else:
                if dificultad in ('fácil', 'facil'):
                    self.adivinaComputadora(facil=True)
                elif dificultad in ('difícil', 'dificil'):
                    self.adivinaComputadora(facil=False)
                break

    def crearJugador(self):
        self.secuencia = []
        numColo = 0
        while numColo < 4:
            print(Fore.GREEN + "Colores: " + Fore.BLUE + "azul = B, " + Fore.YELLOW + "amarillo = Y, " + Fore.RED + "rojo = R, " + Fore.GREEN + "verde = G" + Fore.RESET)
            print("Tienes que ingresar los colores uno por uno. Ejemplo: primero 'R' y presionas enter, luego 'G' y presionas enter, etc.")
            color = input("Ingresa el color (B, Y, G, R): ").upper()
            if color == "B":
                numColo += 1
                self.secuencia.append(self.azul)
            elif color == "G":
                numColo += 1
                self.secuencia.append(self.verde)
            elif color == "Y":
                numColo += 1
                self.secuencia.append(self.amarillo)
            elif color == "R":
                numColo += 1
                self.secuencia.append(self.rojo)
            else:
                print("")
                print(Fore.RED + "Color no válido. Intenta de nuevo." + Fore.RESET)

        print("\n┃ " + ' '.join(self.secuencia) + " ┃" + "  Esta es tu secuencia creada")
        print("")
        decision = input("¿Quieres volver a hacer la secuencia? (S/N): ").lower()
        if decision == "s":
            self.crearJugador()
        else:
            print("Está bien. Tu secuencia es:")
            print("")

    def crearCompu(self):
        self.secuencia = random.choices(self.colores, k=4)
        print(Fore.GREEN + "¡Secuencia creada por la computadora!" + Fore.RESET)

    def adivinaJugador(self):
        print("El jugador crea una secuencia.")
        self.crearCompu()
        intentos = 0
        while intentos < 12:
            print(Fore.GREEN + "Colores: " + Fore.BLUE + "azul = B, " + Fore.YELLOW + "amarillo = Y, " + Fore.RED + "rojo = R, " + Fore.GREEN + "verde = G" + Fore.RESET)
            print("Tienes que ingresar los colores juntos con espacio ejemplo( y b r g )")
            intento = input("Ingresa tu secuencia de colores: ").upper().split()
            intentoDeSecuencia = [self.azul if color == "B" else self.amarillo if color == "Y" else self.verde if color == "G" else self.rojo for color in intento]
            verificadorDeColores = []
            
            for i in range(4):
                if intentoDeSecuencia[i] == self.secuencia[i]:
                    verificadorDeColores.append(Fore.GREEN + "🟢" + Fore.RESET)
                elif intentoDeSecuencia[i] in self.secuencia:
                    verificadorDeColores.append(Fore.YELLOW + "🟡" + Fore.RESET)
                else:
                    verificadorDeColores.append(Fore.RED + "🔴" + Fore.RESET)

        
            if intentos < 12:
                self.tabla[intentos] = [self.azul if color == self.azul else self.amarillo if color == self.amarillo else self.verde if color == self.verde else self.rojo for color in intento]
                self.verificadores[intentos] = verificadorDeColores

            print("\nTabla de intentos:")
            for i in range(12):
                verificador_str = ' '.join(self.verificadores[i])
                print(f"Resultado: ┃ {verificador_str} ┃" )
            print("")

            print("Tu secuencia ingresada: " + ' '.join(intentoDeSecuencia))
            if intentoDeSecuencia == self.secuencia:
                print(Fore.GREEN + "¡Adivinaste la secuencia!" + Fore.RESET)
                break
            intentos += 1
        if intentos == 12:
            print(Fore.RED + "Se acabaron los intentos. La secuencia era: " + ' '.join(self.secuencia) + Fore.RESET)

    def adivinaComputadora(self, facil=True):
        print("El jugador crea una secuencia.")
        time.sleep(1)
        self.crearJugador()
        intentos = 0
        while intentos < 12:
            if facil:
                decisionDeLaCompu = random.choices(self.colores, k=4)
            else:
                decisionDeLaCompu = self.logicaDificil()
                
            verificadorDeColores = []
            for i in range(4):
                if decisionDeLaCompu[i] == self.secuencia[i]:
                    verificadorDeColores.append("🟢")
                elif decisionDeLaCompu[i] in self.secuencia:
                    verificadorDeColores.append("🟡")
                else:
                    verificadorDeColores.append("🔴")
                    
            if intentos < 12:
                self.tabla[intentos] = decisionDeLaCompu
                self.verificadores[intentos] = verificadorDeColores
                self.historial.append((decisionDeLaCompu, verificadorDeColores))

            print("\nTabla de intentos:")
            for i in range(12):
                verificador_str = ' '.join(self.verificadores[i])
                print(f"Intento : ┃ {verificador_str} ┃")

            print("\nSecuencia de la computadora: " + ' '.join(decisionDeLaCompu))
            if decisionDeLaCompu == self.secuencia:
                print(Fore.GREEN + "¡La computadora adivinó la secuencia!" + Fore.RESET)
                break
            intentos += 1
        if intentos == 12:
            print(Fore.RED + "La computadora no pudo adivinar la secuencia." + Fore.RESET)

    def logicaDificil(self):
        if not self.historial:
            return random.choices(self.colores,k=4)
        ultimaSecuencia,UltimaVerificaciones = self.historial[-1]
        nuevaSecuencia = ultimaSecuencia[:]
        for i in range(4):
            if UltimaVerificaciones[i] == "🟢":
                continue
            elif UltimaVerificaciones[i] == "🟡":
                colorResta = [color for color in self.colores if color != ultimaSecuencia[i]]
                nuevaSecuencia[i] = random.choice(colorResta)
            else:
                nuevaSecuencia[i] = random.choice(self.colores)
        return nuevaSecuencia
def main():
    juego = Game()
    # juego.bienvenida()
    juego.elegirModo()

main()