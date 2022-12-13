
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")



#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
dict = {row.letter:row.code for (letter, row) in data.iterrows()}

print(dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word_to_spell = input('Input a word to speel in NATO: ').upper()
print([dict[letter] for letter in word_to_spell])
