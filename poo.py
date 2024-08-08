# profe documente lo que veia que era necesario osea cosas que talves no pueda entender bien a la primera y lo que no documento porque eso es facil de entender 
from colorama import Fore
import random
import time

class Game:
    def __init__(self):
        self.secuencia = []  # Secuencia de colores a adivinar
        self.azul = Fore.BLUE + "🔵" + Fore.RESET  # Color azul
        self.amarillo = Fore.YELLOW + "🟡" + Fore.RESET  # Color amarillo
        self.verde = Fore.GREEN + "🟢" + Fore.RESET  # Color verde
        self.rojo = Fore.RED + "🔴" + Fore.RESET  # Color rojo
        self.colores = [self.azul, self.amarillo, self.verde, self.rojo]  # Lista de colores disponibles
        self.tabla = [["⚪" for _ in range(4)] for _ in range(12)]  # Tabla para registrar los intentos
        self.verificadores = [["⚪" for _ in range(4)] for _ in range(12)]  # Tabla para verificar los resultados
        self.historial = []  # Historial de intentos de la computadora

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
            if dificultad not in ('fácil', 'facil', 'difícil', 'dificil'): #esto es para que solo pueda ingresar eso texto
                print("Por favor, agrega una respuesta correcta.") # y si escribe algo difirente de lo que se pide que la mande ese print
            else:
                # y aqui abajo que si se cumple lo ingresado mande loq que el usuario elegio ya sea dificil o facil
                if dificultad in ('fácil', 'facil'):
                    self.adivinaComputadora(facil=True)
                elif dificultad in ('difícil', 'dificil'):
                    self.adivinaComputadora(facil=False)
                break

    def crearJugador(self):
        # Permite al jugador crear una secuencia de 4 colores.
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
                print(Fore.RED + "Color no válido. Intenta de nuevo." + Fore.RESET)

        print("\n┃ " + ' '.join(self.secuencia) + " ┃" + "  Esta es tu secuencia creada")
        decision = input("¿Quieres volver a hacer la secuencia? (S/N): ").lower()
        if decision == "s":
            self.crearJugador()
        else:
            print("Está bien. Tu secuencia es:")
            print("")

    def crearCompu(self):
        # Crea una secuencia aleatoria de 4 colores para que el jugador adivine.
        self.secuencia = random.choices(self.colores, k=4)
        print(Fore.GREEN + "¡Secuencia creada por la computadora!" + Fore.RESET)

    def adivinaJugador(self):
        # Permite al jugador adivinar la secuencia creada por la computadora.
        print("El jugador crea una secuencia.")
        self.crearCompu()
        intentos = 0
        while intentos < 12:
            print(Fore.GREEN + "Colores: " + Fore.BLUE + "azul = B, " + Fore.YELLOW + "amarillo = Y, " + Fore.RED + "rojo = R, " + Fore.GREEN + "verde = G" + Fore.RESET)
            print("Tienes que ingresar los colores juntos con espacio ejemplo( y b r g )")
            intento = input("Ingresa tu secuencia de colores: ").upper().split()
            
            intentoDeSecuencia = []
            for color in intento:
                if color == "B":
                    intentoDeSecuencia.append(self.azul)
                elif color == "G":
                    intentoDeSecuencia.append(self.verde)
                elif color == "Y":
                    intentoDeSecuencia.append(self.amarillo)
                elif color == "R":
                    intentoDeSecuencia.append(self.rojo)
                else:
                    intentoDeSecuencia.append("⚪")  # Indicador de error si el color no existe
            
            verificadorDeColores = []
            for i in range(4):
                if intentoDeSecuencia[i] == self.secuencia[i]:
                    verificadorDeColores.append(Fore.GREEN + "🟢" + Fore.RESET)
                elif intentoDeSecuencia[i] in self.secuencia:
                    verificadorDeColores.append(Fore.YELLOW + "🟡" + Fore.RESET)
                else:
                    verificadorDeColores.append(Fore.RED + "🔴" + Fore.RESET)

            if intentos < 12:
                self.tabla[intentos] = intentoDeSecuencia
                self.verificadores[intentos] = verificadorDeColores

            self.mostrarTabla(intentos + 1)
            
            if intentoDeSecuencia == self.secuencia:
                print(Fore.GREEN + "¡Adivinaste la secuencia!" + Fore.RESET)
                break
            
            intentos += 1
        
        if intentos == 12:
            print(Fore.RED + "Se acabaron los intentos. La secuencia era: " + ' '.join(self.secuencia) + Fore.RESET)

    def adivinaComputadora(self, facil=True):
        # La computadora intenta adivinar la secuencia creada por el jugador.
        
        #param facil: Determina si la dificultad es fácil (True) o difícil (False).
        print("El jugador crea una secuencia.")
        time.sleep(1)  # Pausa de 1 segundo para permitir que el jugador cree la secuencia.
        self.crearJugador()
        
        intentos = 0
        while intentos < 12:
            # Dependiendo de la dificultad, decide la secuencia de colores.
            if facil:
                # Genera una secuencia aleatoria de 4 colores.
                decisionDeLaCompu = random.choices(self.colores, k=4)
            else:
                # Utiliza una lógica más avanzada para generar la secuencia.
                decisionDeLaCompu = self.logicaDificil()
            
            verificadorDeColores = []
            # Compara la secuencia propuesta por la computadora con la secuencia correcta.
            for i in range(4):
                if decisionDeLaCompu[i] == self.secuencia[i]:
                    verificadorDeColores.append(Fore.GREEN + "🟢" + Fore.RESET)
                elif decisionDeLaCompu[i] in self.secuencia:
                    verificadorDeColores.append(Fore.YELLOW + "🟡" + Fore.RESET)
                else:
                    verificadorDeColores.append(Fore.RED + "🔴" + Fore.RESET)
            if intentos < 12:
                 # Guarda la secuencia propuesta y sus verificaciones en las tablas correspondientes.
                self.tabla[intentos] = decisionDeLaCompu
                self.verificadores[intentos] = verificadorDeColores
                 # Añade el intento y su verificación al historial.
                self.historial.append((decisionDeLaCompu, verificadorDeColores))
            # Muestra la tabla de intentos hasta el intento actual.
            self.mostrarTabla(intentos + 1)
            
            time.sleep(1)
            print("\nSecuencia de la computadora: " + ' '.join(self.tabla[intentos]))
            
            if self.tabla[intentos] == self.secuencia:
                print(Fore.GREEN + "¡La computadora adivinó la secuencia!" + Fore.RESET)
                break
            
            intentos += 1
        
        if intentos == 12:
            print(Fore.RED + "La computadora no pudo adivinar la secuencia." + Fore.RESET)

    def logicaDificil(self):
        # Genera una secuencia en modo difícil basada en el historial de intentos.
        # :return: Una nueva secuencia propuesta por la computadora.
        if not self.historial:
            return random.choices(self.colores, k=4)
        
        ultimaSecuencia, UltimaVerificaciones = self.historial[-1]
        nuevaSecuencia = ultimaSecuencia[:]
        
        for i in range(4):
            if UltimaVerificaciones[i] == Fore.GREEN + "🟢" + Fore.RESET:
                continue
            elif UltimaVerificaciones[i] == Fore.YELLOW + "🟡" + Fore.RESET:
                colorResta = [color for color in self.colores if color != ultimaSecuencia[i]]
                nuevaSecuencia[i] = random.choice(colorResta)
            else:
                nuevaSecuencia[i] = random.choice(self.colores)
        
        return nuevaSecuencia

    def mostrarTabla(self, hasta_intento):
        # Muestra la tabla de intentos y sus resultados.
        print("\nTabla de intentos:")
        for i in range(12):
            verificador_str = ' '.join(self.verificadores[i])
            tabla_str = ' '.join(self.tabla[i])
            if i < hasta_intento:
                print(f"Intento: ┃ {verificador_str} ┃   ┃ {tabla_str} ┃")
            else:
                print(f"Intento: ┃ {' '.join(['⚪']*4)} ┃   ┃ {' '.join(['⚪']*4)} ┃") 

def main():
    juego = Game()
    juego.bienvenida()
    juego.elegirModo()

if __name__ == "__main__":
    main()
