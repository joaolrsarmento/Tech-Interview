# Given to strings, write a function to check if they are one edit (or zero edits) away.
# Edits: insert, remove or replace a character

class Solution:
    """

    We're gonna try convert the shorter string into the longer one
    O(n) -> time complexity
    O(n) -> space complexity
    Where n is the shorter's string length
    """

    def oneAway(self, string1: str, string2: str) -> bool:

        shorter = string1 if len(string1) <= len(string2) else string2
        longer = string2 if len(string1) <= len(string2) else string2

        if len(shorter) == len(longer): return self.oneReplaceAway(shorter, longer)
        if len(shorter) + 1 == len(longer): return self.oneInsertAway(shorter, longer)

        return False

    def oneReplaceAway(self, s1, s2):
        foundDifference = False
        for i in range(len(s1)):

            if s1[i] != s2[i]:
                if foundDifference: return False
                foundDifference = True
        
        return True
    def oneInsertAway(self, s1, s2):
        i1, i2 = 0,0

        insertedAlready = False
        while i1 <= len(s1) and i2 <= len(s2):
            if s1[i1] != s2[i2]:
                if insertedAlready: return False
                insertedAlready = True
                i2+=1
            else:
                i1+=1
                i2+=1

        return True

s1 = input()
s2 = input()

solve = Solution()
print(solve.oneAway(s1, s2))