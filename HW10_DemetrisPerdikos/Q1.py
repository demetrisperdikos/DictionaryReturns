#Demetris Perdikos
# 11/10/2020
# HW 10

def initialLetterCount(wordList ):
    aDict = {}
    for i in range(len(wordList)):
        if wordList[i][0] in aDict:
            aDict[wordList[i][0]] = aDict[wordList[i][0]] + 1
        else:
            aDict[wordList[i][0]] = 1
    return aDict
horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetterCount(horton))