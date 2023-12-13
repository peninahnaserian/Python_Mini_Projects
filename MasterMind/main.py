# generate a 4 color random code
# make the user guess the code
# compare the guess to the code
# tie the game together

import random

COLORS = ["R","G","B","Y","W","O"]
TRIES = 10
CODE_LENGTH = 4

def genreate_code():
    code = []
    
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    
    return code

def guess_code():
    guess = input("Guess: ").upper().split(" ") 