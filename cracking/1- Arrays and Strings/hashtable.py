# Given an array, count the number of pairs (x,y) that |x - y| = k
# Max time complexity: O(n)
# Max space complexity: O(n)

arr = [1,   7,    5,   9,   2,   12,    3]

k = 2

hash = {}
cont = 0
for num in arr:
    hash[num] = True
for num in arr:
    if hash.get(num + k, -1) != -1 or hash.get(num - k, -1) != -1:
        print(num)
        cont += 1
