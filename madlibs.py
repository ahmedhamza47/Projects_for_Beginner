#This is a madlibs game
print('Story 1:')
print("Today I went to the zoo. I saw a(n)_______(adjective)___________(Noun) jumping up and down in its tree. "
    "He _____________(verb, past tense) __________(adverb) \nthrough the large tunnel that led to its _______(adjective)"
    "__________(noun). I got some peanuts and passed them through the cage to a gigantic gray\n_______(noun)towering above my head. "
    "Feeding that animal made"
    "me hungry. I went to get a __________(adjective) scoop"
    "of ice cream. It filled my stomach.\nAfterwards I had to"
    "__________(verb) __________ (adverb) to catch our bus."
    "When I got home I __________(verb, past tense) my "
    "mom for a __________(adjective)\nday at the zoo. ")

print('Guess the missing words in the story:')
words = []
for i in range(12):
    word = input()
    words.append(word)

print('Your story is:\n')
print("Today I went to the zoo. I saw an",words[0],words[1]," jumping up and down in its tree. "
    "He",words[2],words[3]," \nthrough the large tunnel that led to its ",words[4],
      "",words[5],". I got some peanuts and passed them through the cage to a gigantic gray\n",words[6],"towering above my head. "
    "Feeding that animal made"
    " me hungry. I went to get a ",words[7]," scoop"
    " of ice cream. It filled my stomach.\nAfterwards I had to"
    "",words[8],words[9]," to catch our bus."
    "When I got home I",words[10],"my"
    "mom for a",words[11],"\nday at the zoo.")
