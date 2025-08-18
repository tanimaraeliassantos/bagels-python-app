#Deductive logic game on which
#  you must guess a secret three-digit number based on clues.
#The game offers one of the following hints in response to
#  your guess: "Pico" when your guess has a correct digit in the
#wrong place, "Fermi" when your guess has a correct digit in the\
#correct place, and "Bagels" if your guess has no correct digits.
#You have 10 tries to guess the secret number.

import random
#importing access to random operations
NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Bagels, a deductive logic game.
          
          I have a {}-digit number with no repeated digits.
          Try too guess what it is. Here are some clues:
           When I say:    That means:
           Pico           One digit is correct but in the wrong position.
           Fermi          One digit is correct and in the right position.
           Bagels         No digit is correct.

           For example, if the secret number was 248 and your guess was 843,
           the clues would be Fermi Pico.'''.format(NUM_DIGITS))