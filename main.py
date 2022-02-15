import pandas
nato_dict = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = nato_dict.set_index("letter").to_dict()
nato_dict = {letter: code for (letter, code) in nato_dict["code"].items()}
user_input = input("Which word do you need to spell phonetic?: ").upper()
word = [char for char in user_input]
spell_word = [nato_dict[letter] for letter in word]
print(spell_word)