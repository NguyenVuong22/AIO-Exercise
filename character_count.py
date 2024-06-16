def character_count(word):
    character_statistic = {}

    for i in range(len(word)):
        character_statistic.update({word[i]: word.count(word[i])})
    return character_statistic


assert character_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
print(character_count('Happiness'))
print(character_count('smiles'))
