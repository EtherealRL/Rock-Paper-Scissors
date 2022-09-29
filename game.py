import random as r
import os
from colorama import Fore

class Game():
    def __init__(self):
        self.options = {"1": "Rock", "2": "Paper", "3": "Scissors"}
        self.ai_choice = None
        self.choice = None
        self.play_again = True
        self.run()
    
    def get_choice(self):
        while self.choice not in self.options:
            self.choice = input("1. Rock\n2. Paper\n3. Scissors\nChoose an option: ")
            os.system('cls' if os.name == 'nt' else 'clear')
        self.choice = self.options[self.choice]
    
    def get_ai_choice(self):
        self.ai_choice = r.choice(list(self.options.values()))

    def check_winner(self):
        if self.choice == self.ai_choice:
            print(f" You both chose {self.choice}. It's a tie!")
        elif self.choice == "Rock":
            if self.ai_choice == "Paper":
                print(Fore.RED, "Paper covers rock! You lose.")
            else:
                print(Fore.GREEN, "Rock smashes scissors! You win!")
        elif self.choice == "Paper":
            if self.ai_choice == "Scissors":
                print(Fore.RED, "Scissors cuts paper! You lose.")
            else:
                print(Fore.GREEN, "Paper covers rock! You win!")
        elif self.choice == "Scissors":
            if self.ai_choice == "Rock":
                print(Fore.RED, "Rock smashes scissors! You lose.")
            else:
                print(Fore.GREEN, "Scissors cuts paper! You win!")
        print(Fore.RESET)

    def ask_play_again(self):
        while True:
            self.play_again = input(" Would you like to play again? (Y/N): ").upper()
            os.system('cls' if os.name == 'nt' else 'clear')
            if self.play_again == "Y":
                break
            elif self.play_again == "N":
                self.play_again = False
                break

    def run(self):
        while self.play_again:
            self.get_choice()
            self.get_ai_choice()
            self.check_winner()
            self.ask_play_again()