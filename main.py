import pandas
nl_phonetic_dict = pandas.read_csv("nl_phonetic_alphabet.csv")
nl_phonetic_dict = {row.letter: row.code for (index, row) in nl_phonetic_dict.iterrows()}
user_input = input("Which word do you need to spell phonetic?: ").upper()
word = [char for char in user_input]
spell_word = [nl_phonetic_dict[letter] for letter in word]
print(spell_word)
