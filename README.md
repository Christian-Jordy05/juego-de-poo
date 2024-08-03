# juego-de-poo

import random
from colored import fg, attr

COLORS = ['red', 'blue', 'green', 'yellow']
COLOR_MAP = {
    'red': fg('red'),
    'blue': fg('blue'),
    'green': fg('green'),
    'yellow': fg('yellow'),
    'white': fg('white'),
    'light_yellow': fg('light_yellow')
}

class Board:
    def _init_(self):
        self.board = [[' ' for _ in range(5)] for _ in range(12)]
    
    def display(self):
        for row in self.board:
            print(' '.join(row))
    
    def update(self, turn, guess, feedback):
        for i in range(4):
            self.board[turn][i] = COLOR_MAP[guess[i]] + '⬤' + attr('reset')
        self.board[turn][4] = ''.join(feedback)  # Combine feedback into one string for better display

class CodeMaker:
    def _init_(self, code=None):
        self.code = code if code else [random.choice(COLORS) for _ in range(4)]

    def provide_feedback(self, guess):
        feedback = ['⬤' for _ in range(4)]
        temp_code = self.code.copy()
        temp_guess = guess.copy()

        # Green feedback for correct color and position
        for i in range(4):
            if guess[i] == self.code[i]:
                feedback[i] = COLOR_MAP['green'] + '⬤' + attr('reset')
                temp_code[i] = temp_guess[i] = None
        
        # Light yellow feedback for correct color but wrong position
        for i in range(4):
            if temp_guess[i] and temp_guess[i] in temp_code:
                feedback[i] = COLOR_MAP['light_yellow'] + '⬤' + attr('reset')
                temp_code[temp_code.index(temp_guess[i])] = None

        return feedback

class CodeBreaker:
    def make_guess(self):
        while True:
            guess = input("Introduce tu intento (cuatro colores separados por espacio): ").split()
            if len(guess) == 4 and all(color in COLORS for color in guess):
                return guess
            print("Entrada no válida. Asegúrate de ingresar cuatro colores válidos separados por espacios.")

class Game:
    def _init_(self):
        self.board = Board()
        self.turns = 0
        self.code_maker = None
        self.code_breaker = CodeBreaker()

    def setup(self):
        while True:
            role = input("¿Deseas ser el creador del código o el adivinador? (creador/adivinador): ").strip().lower()
            if role == 'creador':
                while True:
                    code = input("Introduce el código secreto (cuatro colores separados por espacio): ").split()
                    if len(code) == 4 and all(color in COLORS for color in code):
                        self.code_maker = CodeMaker(code)
                        break
                    print("Entrada no válida. Asegúrate de ingresar cuatro colores válidos separados por espacios.")
                break
            elif role == 'adivinador':
                self.code_maker = CodeMaker()
                break
            print("Entrada no válida. Por favor, introduce 'creador' o 'adivinador'.")

    def play(self):
        self.setup()
        while self.turns < 12:
            print(f"\nTurno {self.turns + 1}")
            self.board.display()
            guess = self.code_breaker.make_guess()
            feedback = self.code_maker.provide_feedback(guess)
            self.board.update(self.turns, guess, feedback)
            if all(f == COLOR_MAP['green'] + '⬤' + attr('reset') for f in feedback):
                self.board.display()
                print("¡Felicidades! Adivinaste el código.")
                return
            self.turns += 1
        self.board.display()
        print(f"Fin del juego. El código era: {' '.join(self.code_maker.code)}")


game = Game()
game.play()