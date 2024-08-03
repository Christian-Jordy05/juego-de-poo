from colored import fg, attr
class Poo:
    def __init__(self,nombre):
        nombre = nombre 
    pass
    def bienvenida():
        print(f"{fg('green')}bienvenido usuario listo para jugar{attr('reset')}")
        veri = input("S/N: ")
        if veri == "S":
            print(f"{fg('green')}okey, pero antes de empezar el juego, ¿me puedes decir tu nombre?{attr('reset')}")
            NombreDeUser = input("Dime tu nombre: ")
            print(f"{fg("green")}hola {NombreDeUser}, el juego ya va a empezar{attr("reset")}")
        else:
            print(f"{fg('red')}adios usuario, que tengas un excelente día{attr('reset')}")
def main():
  Poo.bienvenida()
        
pass
        
    
if __name__ == "__main__":
 main()









# # class Game():
# #     #Aquí va todo el juego, obviamente dividido en distintas funciones.
# #     def __init__(self, nombre):
# #         self.nombre = nombre
# #         self._secuencia = []
# #         print(f"¿Quieres entrar")
# # def main():
# #     #Aquí va el orden en que se presenta el juego.
# #     print(f"Orden")
# # if __name__ == "__main__":
# #     # Inicializador del archivo.
# #     main()



# import random
# from colored import fore, back, style

# class Mastermind:
#     def _init_(self):
#         self.colors = ["red", "blue", "green", "yellow"]
#         self.attempts = 12
#         self.code_length = 4
#         self.board = [[" " for _ in range(self.code_length + 1)] for _ in range(self.attempts)]
    
#     def set_code(self):
#         self.code = [random.choice(self.colors) for _ in range(self.code_length)]

#     def get_feedback(self, guess):
#         feedback = [" " for _ in range(self.code_length)]
#         code_copy = self.code.copy()

#         for i in range(self.code_length):
#             if guess[i] == code_copy[i]:
#                 feedback[i] = "green"
#                 code_copy[i] = None

#         for i in range(self.code_length):
#             if feedback[i] != "green" and guess[i] in code_copy:
#                 feedback[i] = "orange"
#                 code_copy[code_copy.index(guess[i])] = None

#         return feedback

#     def update_board(self, turn, guess, feedback):
#         self.board[turn] = guess + feedback

#     def display_board(self):
#         for row in self.board:
#             for color in row:
#                 if color in self.colors:
#                     print(fore(color) + "⬤" + style("reset"), end=" ")
#                 elif color == "green":
#                     print(fore("green") + "⬤" + style("reset"), end=" ")
#                 elif color == "orange":
#                     print(fore("orange") + "⬤" + style("reset"), end=" ")
#                 else:
#                     print("⬤", end=" ")
#             print()
#         print()

#     def player_guess(self):
#         while True:
#             guess = input("Enter your guess (four colors separated by space): ").split()
#             if len(guess) == self.code_length and all(color in self.colors for color in guess):
#                 return guess
#             print("Invalid input, try again.")

#     def player_set_code(self):
#         while True:
#             code = input("Enter the secret code (four colors separated by space): ").split()
#             if len(code) == self.code_length and all(color in self.colors for color in code):
#                 return code
#             print("Invalid input, try again.")

#     def computer_guess_random(self):
#         return [random.choice(self.colors) for _ in range(self.code_length)]

#     def computer_guess_brute_force(self, previous_guesses):
#         all_combinations = [[a, b, c, d] for a in self.colors for b in self.colors for c in self.colors for d in self.colors]
#         valid_combinations = [comb for comb in all_combinations if all(self.get_feedback(guess) == self.get_feedback(comb) for guess in previous_guesses)]
#         return random.choice(valid_combinations)

#     def computer_guess_smart(self, previous_guesses):
#         # Implement a smarter strategy based on some researched algorithms
#         # This is a placeholder for demonstration
#         return self.computer_guess_random()

#     def play(self):
#         role = input("Do you want to be the code maker or guesser? (maker/guesser): ").strip().lower()
#         if role == "maker":
#             self.code = self.player_set_code()
#             previous_guesses = []
#             for turn in range(self.attempts):
#                 guess = self.computer_guess_random()
#                 previous_guesses.append(guess)
#                 feedback = self.get_feedback(guess)
#                 self.update_board(turn, guess, feedback)
#                 self.display_board()
#                 if feedback == ["green"] * self.code_length:
#                     print("Computer guessed the code!")
#                     return
#             print("Computer failed to guess the code.")
#         else:
#             self.set_code()
#             for turn in range(self.attempts):
#                 guess = self.player_guess()
#                 feedback = self.get_feedback(guess)
#                 self.update_board(turn, guess, feedback)
#                 self.display_board()
#                 if feedback == ["green"] * self.code_length:
#                     print("You guessed the code!")
#                     return
#             print(f"You failed to guess the code. The code was: {' '.join(self.code)}")
# def main():
#     Mastermind.play()
# if __name__ == "_main_":
#    main()