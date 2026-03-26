## Personal Programming Project - Alvin Lee

from colorama import Fore, Back, Style ## pip install colorama
from random import randint
import random
from PyDictionary import PyDictionary ## pip install PyDictionary
dictionary = PyDictionary

# store letters values
freq = {"E": 12,
       "A": 9,
       "I": 9,
       "O": 8,
       "N": 6,
       "R": 6,
       "T": 6,
       "L": 4,
       "S": 4,
       "U": 4,
       "D": 4,
       "G": 3,
       "B": 2,
       "C": 2,
       "M": 2,
       "P": 2,
       "F": 2,
       "H": 2,
       "V": 2,
       "W": 2,
       "Y": 2,
       "K": 1,
       "J": 1,
       "X": 1,
       "Q": 1,
       "Z": 1,
       " ": 2}

# avaliables letters to give
letters = []
for letter in freq:
    for i in range(freq[letter]):
        letters.append(letter)

points = {1: ["E", "A", "I", "O", "N", "R", "T", "L", "S", "U"],
         2: ["D", "G"],
         3: ["B", "C", "M", "P"],
         4: ["F", "H", "V", "W", "Y"],
         5: ["K"],
         8: ["J", "X"],
         10: ["Q", "Z"]}

def update_letters(letters):
    words = [[] for _ in range(2)]
    for i in range(2):
        word = words[i]
        for i in range(7):
            random.shuffle(letters)
            l = letters.pop()
            word.append(l)

    return words
        
def create_board():
    board = []
    for i in range(15):
        board.append("-"*61)
        board.append("|   "*15 + "|")
    board.append("-"*61)

    return board

def display_board(b):
    # displays board with letter and numbers
    disboard = []
    disboard.append("     A   B   C   D   E   F   G   H   I   J   K   L   M   N   O")
    for row in range(len(b)):
        if row % 2 == 1:
            front = str((row+1)//2)
            if len(front) == 1:
                front += "  "
            else:
                front += " "
        else:
            front = "   "

        disboard.append(front + b[row])

    for row in disboard:
        print(row)

def choose_first_player():
    pass

def bot_turn():
    pass

def enter_letters(words):
    print("Turn: Player")
    tempwords = words[:]
    flag = True
    createword = []
    while flag and len(words) > 0:
        valid = False
        while not valid:
            print("Your letters:", ", ".join(word for word in tempwords))
            place = input("Enter placement:\n> ").split(" ")
            let = place[0]
            valid = True
            try:
                tempwords.remove(let)
                createword.append(place)
                valid = True
                con = input("Continue? (y/n): ")
                if con == "n":
                    flag = False
                    return createword, tempwords
            except:
                print("You don't have this letter!")

def check_valid(words):
    ref_column = words[1][1][0]
    ref_row = words[1][1][1]
    same_row = True
    same_column = True
    for pos in words:
        if ref_column != pos[1][0]: ## column
            same_row = False
        if ref_row != pos[1][1]: ## rows
            same_column = False
    if same_row or same_column:
        print("Word positions valid")
        return True
    else:
        print("Word positions not valid")
        return False, False

def player_first_turn():
    pass

def display_score(pscore, bscore):
    print("Score")
    print("Player:", pscore)
    print("Bot:", bscore)
    print("\n")

def introduction():
    print("WELCOME TO SCRABBLE!!")
    print("Enter turn with letter and position of letter (e.g. J B1)\n")
    print("Colour multiplier:")
    print(Back.RED + "-" + Style.RESET_ALL + " 3x word score")
    print(Back.YELLOW + "-" + Style.RESET_ALL + " 3x word score")
    print(Back.BLUE + "-" + Style.RESET_ALL + " 3x word score")
    print(Back.CYAN + "-" + Style.RESET_ALL + " 3x word score\n")

def main():
    introduction()
    board = create_board()
    display_board(board)
    plr_words, bot_words = update_letters(letters)
    pscore, bscore = 0, 0
    while len(letters) > 0:
        display_score(pscore, bscore)
        val1, val2 = False, False
        while not (val1 or val2):
            player_letters, wordsleft = enter_letters(plr_words)
            val1, val2 = check_valid(player_letters)
        plr_words = wordsleft

main()