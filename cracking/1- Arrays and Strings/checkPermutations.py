# Given 2 strings, check if one if other's permutation


# O(n) - time complexity
# O(n) - space complexity

A = 'idhjaeiejkefoksef'
B = 'idhjaeiejkefofkse'

if len(A) != len(B):
    print('False')

hashTable = {}

for el in list(A):
    if hashTable.get(el, -1) == -1:
        hashTable[el] = 1
    else:
        hashTable[el] += 1

for el in list(B):
    if hashTable.get(el, -1) == -1:
        print('aFalse')
        break
    else:
        if hashTable[el] == 0:
            print('bFalse')
            break
        else:
            hashTable[el] -= 1

print('Sure')

# O(n) - time complexity
# O(1) - space complexity

isPermutation = True

letters = [0] * 128

for el in A:
    letters[ord(el)] += 1
for el in B:
    letters[ord(el)] -= 1
    if letters[ord(el)] < 0:
        isPermutation = False
        break

if isPermutation:
    print(True)
else:
    print(False)

