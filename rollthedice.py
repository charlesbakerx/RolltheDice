"""
Author: Charles Baker
Date Created: 11-08-2023
Description: A simple program that rolls two dice and outputs the sum,
                then asks the user if they would like to roll again.
Pseudocode:
    Inputs: Y/N from the user
    Processes: Generate two random numbers and return them
    Outputs: The value of both dice and their sum.
"""
import random
import os
from time import sleep

# Rolling dice ascii art by Morfina from https://www.asciiart.eu/miscellaneous/dice
rollingDice = (
    "\t\t       (( _______\n             _______     /\\O    O \\\n            /O     /\\   /  \\       \\\n      "
    "     /"
    "   O  /O \\ / O  \\O_____O\\ ))\n        ((/_____O/    \\     /O      /\n          \\O    O\\    / \\  /   O  "
    " /\n           \\O    O\\ O/   \\/______O/\n            \\O____O\\/ ))          ))\n          ((\n")

dieValues = {
    "1": (" _______\n"
          "|       |\n"
          "|   •   |\n"
          "|       |\n"
          " ‾‾‾‾‾‾‾"),
    "2": (" _______\n"
          "| •     |\n"
          "|       |\n"
          "|     • |\n"
          " ‾‾‾‾‾‾‾\n"),
    "3": (" _______\n"
          "| •     |\n"
          "|   •   |\n"
          "|     • |\n"
          " ‾‾‾‾‾‾‾\n"),
    "4": (" _______\n"
          "| •   • |\n"
          "|       |\n"
          "| •   • |\n"
          " ‾‾‾‾‾‾‾\n"),
    "5": (" _______\n"
          "| •   • |\n"
          "|   •   |\n"
          "| •   • |\n"
          " ‾‾‾‾‾‾‾\n"),
    "6": (" _______\n"
          "| •   • |\n"
          "| •   • |\n"
          "| •   • |\n"
          " ‾‾‾‾‾‾‾\n")
}


def game_loop():
    while True:
        print("You toss the dice...")
        print(rollingDice)
        sleep(2)
        clear_term()
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        result = die1 + die2
        display_dice(die1, die2)
        a_an = "an" if result == 8 or result == 11 else "a"
        print(f"You rolled {a_an} {result} with a {die1} and {die2}")
        response = input("Would you like to roll the dice again (y/n)? ")
        if response.lower() == 'y':
            clear_term()
            continue
        else:
            clear_term()
            break


def display_dice(die1, die2):
    die1_lines = dieValues[str(die1)].splitlines()
    die2_lines = dieValues[str(die2)].splitlines()
    for die1Line, die2line in zip(die1_lines, die2_lines):
        print("\t", die1Line, "\t", die2line)


def clear_term():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')


print("\t\t================")
print("\t\t Roll the Dice!")
print("\t\t================")
game_loop()
