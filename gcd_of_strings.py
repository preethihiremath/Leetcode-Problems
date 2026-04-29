# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"

# Output: "ABC"

import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        n1=len(str1)
        n2=len(str2)
        n=min(n1,n2)
        gcd=""

        # This is a mathematical property of "periodic" strings. 
        # If two strings share a common base pattern, it doesn't matter which
        # order you stick them together; the resulting sequence will be 
        # identical

        if(str1 + str2 == str2 + str1):
            gcd_len = math.gcd(len(str1), len(str2))

            gcd = str1[:gcd_len]

        return gcd