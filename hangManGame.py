import random


def ranWordGen() -> str:
    wordList = ["kaktusz","szivárvány","pogácsa","esernyő","paprika","gombóc","cseresznye","pillangó","Missisipi"]
    return random.choice(wordList)

wordTemplate = list()
word = ranWordGen()
for i in range(len(word)): #List comprehension (később)
    wordTemplate.append('_')
    print()
print(' '.join(wordTemplate))
print('\nTaláld ki a szót! 10 próbálkozásod van betűk megadására!')
tipp = input('Az ön tippje: ')

if tipp not in word:
    print('Rossz')
else:
    for i in range(len(word)):
        if word[i] == tipp:
            wordTemplate[i] == tipp

print(' '.join(wordTemplate))

print()
input('Press Enter to exit!')