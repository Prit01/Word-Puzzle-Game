#         # Word Puzzle Game
# Problem Statement: You have to write a Word Puzzle Game in which the user has to form
# the correct word out of a given set of characters. In the game the user has to solve this
# puzzle for 5 words, one at a time. Problem words are stored in a list and appear to the user
# in random sequence. Give the user score +1 for each correct answer and give -1 for each
# wrong answer. At last print the final score. You can store any number of words in the list, but
# in each round of the game only 5 words are shown to the user.
# Sample output of the game:
# Arrange the letters to form a valid word:
# RAEHTF
# Father
# Correct
# Arrange the letters to form a valid word:
# KABRE
# Barke
# Wrong
# Arrange the letters to form a valid word:
# CYROTNU
# Cry
# Wrong
# Arrange the letters to form a valid word:
# RENEG
# green
# Correct
# Arrange the letters to form a valid word:
# OAERELANP
# aeroplane
# Correct
# Net Score is 1


import random


words = ["Father", "Bark", "Cry", "Green", "Aeroplane", "Python"]


def select_words(words_list):
    random.shuffle(words_list)
    return words_list[:5]

def play_game():
    score = 0
    selected_words = select_words(words)
    for word in selected_words:
        # Shuffle the letters of the word
        shuffled_letters = list(word)
        random.shuffle(shuffled_letters)
        shuffled_word = "".join(shuffled_letters)
        # Ask the user to 
        print("Arrange the letters to form a valid word:")
        print(shuffled_word)
        user_word = input().strip().capitalize()
        
        if user_word == word:
            print("Correct")
            score += 1
        else:
            print("Wrong")
            score -= 1
    # Print Score final 
    print("Net Score is", score)
play_game()
