# Deductive logic game on which
#  you must guess a secret three-digit number based on clues.
# The game offers one of the following hints in response to
#  your guess: "Pico" when your guess has a correct digit in the
# wrong place, "Fermi" when your guess has a correct digit in the\
# correct place, and "Bagels" if your guess has no correct digits.
# You have 10 tries to guess the secret number.

import random
# importing access to random operations
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

    while True:  # Main game loop.
        # This stores the secret number the player needs to guess:
        secretNum = getSecretNum()
        print('I have thought up a number')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            #Keep looking until they enter a valid guess:
            while len(guess) !=NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('>')
            
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789')  # Create a list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffle them into random order
    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
        return secretNum
