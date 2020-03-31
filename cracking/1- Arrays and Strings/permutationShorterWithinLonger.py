# Given 2 strings (one shorther than the other) find all permutations
# of the shorter string within the longer one. Print the location of each permutation
# Can you do in O(n) which n is the lenght of the longer one?

s = 'abbc'
bs = 'cbabadcbbabbcbabaabccbabc'

perm = []
l = len(s)
for a in range(l):
    for b in range(a,l):
        for c in range(b, l):
            for d in range(c, l):
                perm.append(s[a] + s[b] + s[c] + s[d])
index = 0

while index + l < len(bs):
    for per in perm:
        if per == bs[index:index + l]:
            print(per, index)
    index += 1