# 1768. Merge Strings Alternately
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

 

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1,l2=len(word1),len(word2)
        full = word1 + word2
        final =""
        i=0
        w2=l1

        while(i < min(l1,l2)):
            final+=full[i]
            final+=full[w2]
            i=i+1
            w2=w2+1
            print(final)
        if (l1 > l2):
            su = word1[i:]
            print(su)
            final+=su
        else: 
            su = word2[i:]
            print(su)
            final+=su
        return final
    
# HOW TO OPTIMIZE
# FINAL+= TAKES O(N2) TIME COMPLEXITY, INSTEAD USE A LIST AND JOIN IT AT THE END TO GET O(N) TIME COMPLEXITY
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1,l2=len(word1),len(word2)
        res=[]
        n= min(l1,l2)

        for i in range(0,n):
            res.append(word1[i])
            res.append(word2[i])
            
        res.append(word1[n:])
        res.append(word2[n:])
        return "".join(res)