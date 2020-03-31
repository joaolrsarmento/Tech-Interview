# Given two arrays with the same length, find the common elements between them.
# Can you do in O(n)?

ar1 = [13, 27, 35, 40, 49, 55, 59]
ar2 = [17, 35, 39, 40, 55, 58, 60]

hashTable = {}

for el in ar1:
    hashTable[el] = True

for el in ar2:
    if hashTable.get(el, False):
        print(el)