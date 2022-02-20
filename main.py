import pandas
nl_phonetic_dict = pandas.read_csv("nl_phonetic_alphabet.csv")
nl_phonetic_dict = {row.letter: row.code for (index, row) in nl_phonetic_dict.iterrows()}
def alfabet():
    try:
        user_input = input("Welk woord wil je spellen met het telefoonalfabet?: ").upper()
        word = [char for char in user_input]
        spell_word = [nl_phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Graag alleen letters uit het alfabet invoeren")
        alfabet()
    else:
        print(spell_word)
alfabet()
