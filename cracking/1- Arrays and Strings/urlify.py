# Given an string, replace all spaces with '%20'

# O(n^2) - time complexity
# O(n) - space complexity

string = 'Mr John Smith       '
length = 13

auxiliarList = list(string[:length:])

for i in range(len(auxiliarList)):
    if auxiliarList[i] == ' ':
        del auxiliarList[i]
        auxiliarList.insert(i, '%20')

print(''.join(auxiliarList))

# Implemented in O(n) and O(n) in C++. Check at urlfy.cpp.

