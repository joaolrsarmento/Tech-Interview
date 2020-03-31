# Implement an algorithm to determine if a string has all unique characters.
# What if you can't use data structures

getString = input()

# O(n^2) - time complexity
# O(1) - space complexity
# Without using data structures


for a in range(len(getString)):
    for b in range(a + 1, len(getString)):
        if getString[a] == getString[b]:
            print('not unique')

print('unique')

# O(n) - time complexity
# O(n) - space complexity

hashTable = {}

for a in list(getString):
    if hashTable.get(a, False):
        print('not unique')
    else:
        hashTable[a] = True

print('unique') 

# O(nlogn) - time complexity
# O(1) - space complexity
# Without using data structures

getString = sorted(getString)

ch = getString[0]
cont = -1
for c in getString:
    if cont == -1:
        cont = 0
        continue
    if c == ch:
        print('not unique')
    ch = c

print('unique')