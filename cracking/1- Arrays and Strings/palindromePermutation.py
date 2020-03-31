# Given a string, write a function to check if is a permutation of palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# The palindrome shouldn't be limited to just dictionary words.

string = 'tactcoa'

# O(n.n!) -> time complexity
# O(n!) -> space complexity

def permutations(string: str) -> list:
    perm = []

    if len(string) == 1 or len(string) == 0:
        return [string]
    
    for i in range(len(string)):
        ans = permutations(string[0:i] + string[i+1:])
        for pos in ans:
            perm.append(string[i] + pos)
    return perm

getPermutations = permutations(string)

for permutation in getPermutations:
    if permutation == permutation[::-1]:
        print('Palindrome: ', permutation)

# O(n) -> time complexity
# O(1) -> space complexity

table = [0] * 26
odd = 0
for s in string:
    table[ord(s) - ord('a')] += 1
    if table[ord(s) - ord('a')] % 2:
        odd += 1
    else:
        odd -= 1
if odd <= 1:
    print('Palindrome')
else:
    print('Not a palindrome')