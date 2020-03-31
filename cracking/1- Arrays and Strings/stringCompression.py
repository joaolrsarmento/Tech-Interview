# Given, return the same string using the count of repeated characters if it is compressed
# else, return the original string
# Example: s = 'aaabbcc' --> return 'a3b2c2'; s = 'abc' --> return 'abc';

class Solution:

    """
    Solves the problem in O(n)
    """

    def stringCompression(self, s: str) -> str:
        compressedString = ''

        
        consecutive = 0
        for i in range(len(s)):
            consecutive += 1

            if i + 1 >= len(s) or s[i] != s[i+1]:
                compressedString += s[i] + str(consecutive)
                consecutive = 0

        return compressedString if len(compressedString) < len(s) else s
s = input()

solve = Solution()

print(solve.stringCompression(s))