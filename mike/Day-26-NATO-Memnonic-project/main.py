import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data_file = "nato_phonetic_alphabet.csv"
data = pandas.read_csv(data_file)

code_dict = {item.letter:item.code for (index, item) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("What is the word:").strip().upper()

for letter in user_input:
    print(letter, "-", code_dict[letter])



