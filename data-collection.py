# indexed
varList = [3, 2, 1]

print(varList)
del varList[0]
print(varList[0])

# const
varTuple = (6, 5, 4)

print(varTuple)
# del varTuple[0] doesn't work
print(varTuple[0])

# unique
varSet = {9, 8, 7, 9}
# del varSet[0] doesn't work
varSet1 = {10}

print(varSet)
print(varSet.intersection(varSet1))

# object

varDict = {
    'name': 'Jamaluddin Rumi',
    'achievement': 'have build a business successfully'
}

print(varDict)
del varDict['name']
print(varDict)
print(varDict['achievement'])