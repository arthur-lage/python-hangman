import random
import string
from words import words

def choose_and_filter_word():
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word

def split(word):
    return list(word)

word = choose_and_filter_word()
used_letters = []
correct_letters = []
alphabet = string.ascii_uppercase
chances = 5

print("="*30)
print("Welcome to the Python Hangman!")
print("="*30)
print(word)

while chances > 0:
    letter_input = str(input("Guess a letter: "))
    if letter_input not in used_letters:
        if letter_input in split(word):
            print(f"Attempts left: {chances}")
            used_letters.append(letter_input)
            for char_count in range(word.count(letter_input)):
                correct_letters.append(letter_input)
            print(f"Letter '{letter_input}' is part of the secret word!")
            if len(correct_letters) == len(word):
                break
        elif letter_input == '':
            print("You can't use empty characters!")
        else:
            print(f"Attempts left: {chances}")
            chances -= 1
            used_letters.append(letter_input)
            print(f"Letter '{letter_input}' is not part of the secret word!")
    else:
        print(f"Letter '{letter_input}' was already used!")
if chances == 0:
    print(f"Sorry! You lost the game. The word was: {word.upper()}")
print(f"You won the game! The word is: {word.upper()}")
print("="*30)
print("**************END*************")
print("="*30)