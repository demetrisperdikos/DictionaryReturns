#Demetris Perdikos
# 11/10/2020
# HW 10

def initialLetters(wordList):
    dictionary={}
    for word in wordList:
        if not word[0] in dictionary:
            dictionary[word[0]]=[word]
        elif word not in dictionary[word[0]]:
            dictionary[word[0]].append(word)
    return dictionary

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say', 'wit']
print(initialLetters(horton))
