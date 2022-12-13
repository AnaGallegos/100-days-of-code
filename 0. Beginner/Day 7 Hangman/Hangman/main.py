from random import *

print("Welcome to Hangman!")
word_list = ["sister", "lady", "law", "engineering", "marriage", "judgment", "sir", "reaction", "sympathy", "suggestion", "comparison", "presentation", "energy", "efficiency", "competition", "news", "atmosphere", "director", "republic", "imagination", "decision", "emotion", "vehicle", "economics", "secretary", "understanding", "data", "delivery", "insurance", "painting", "map", "disease", "government", "variation", "lake", "payment", "oven", "hotel", "fortune", "mixture", "ear", "strategy", "city", "feedback", "recording", "indication", "promotion", "coffee", "magazine", "health"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
endgame = False
lives = 6

#choosing a word
word_chosen = word_list[randrange(0, len(word_list))]

#making the word a list
word_encrypted = []
for item in word_chosen:
        word_encrypted.append('_')

print(f"{' '.join(word_encrypted)}")  
endgame = False
lives = 6
while endgame == False:
  
    #inputting a letter
    guess = input('Wich letter is in the word? ').lower()

    for position in range(len(word_chosen)):
        letter = word_chosen[position]
        if letter == guess:
            word_encrypted[position] = letter  
    
    if guess not in word_chosen:
        lives -= 1
        print(f'You have {lives} lives')
        if lives < 1:
            endgame = True
            print(f"You lose, the word was {word_chosen}")

    print(stages[lives])

    print(f"{' '.join(word_encrypted)}")    

    if '_' not in word_encrypted:
        endgame = True
        print('You win! :D')
    

            

