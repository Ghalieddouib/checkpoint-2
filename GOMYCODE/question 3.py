n = int(input('Entrez une valeur :'))
MyDict = {}
if n > 1:
    for i in range (1, n+1):
        MyDict[i] = i*i
print(MyDict)


