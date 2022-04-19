#Demetris Perdikos
# 11/10/2020
# HW 10

def shareALetter(wlist):
    d = {}
    for i in wlist:
        if i not in d:
            l = []
            for j in i:
                for k in wlist:
                    if j in k:
                        if k not in l:
                            l.append(k)
            d[i] = l
    return d

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(shareALetter(horton))