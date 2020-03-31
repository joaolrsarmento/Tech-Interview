# Print all solutions to the equation a^3 + b^3 = c^3 + d^3, where 1 <= a,b,c,d <= 1000
# Max time complexity: O(n^2)

n = 1000

# This hashtable stores the possible results and the pairs that can generate those results
# For example, ans[key] = [pair1, pair2, pair3, pair4], means:
# key = pair1 ^ 3 = pair2 ^ 3 = pair3 ^ 3 = pair4 ^ 3

ans = {}

for c in range(1,n+1):
    for d in range(c, n+1):
        res = c ** 3 + d ** 3
        if ans.get(res, -1) == -1:
            ans[res] = [(c,d)]
        else:
            ans[res].append((c,d))
cont = 0
for res in ans:
    for pair1 in ans[res]:
        for pair2 in ans[res]:
            if pair1 != pair2:
                if cont%2:
                    print(pair1, pair2)
                cont+=1
