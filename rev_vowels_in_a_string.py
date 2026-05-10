# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

class Solution:
    def reverseVowels(self, s: str) -> str:
        l1 = ['a','e','i','o','u','A','E','I','O','U']
        left = 0
        right = len(s) -1
        sr=list(s)

        while left < right:
            if (sr[left] in l1) and (sr[right] in l1):
                temp = sr[left] 
                sr[left] = sr[right]
                sr[right] = temp
                left=left+1
                right=right-1
            if(sr[left] not in l1):
                left=left+1
            if(sr[right] not in l1):
                right = right -1
        return "".join(sr)

class Solution2:
    def reverseVowels(self, s: str) -> str:
        
        #get the vowles
        #reverse and add them to the arrary
        #insert that arrary in that position
        value=[]
        index=[]
        for i in range(len(s)):
            if(s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u'
            or s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U' ):
                value.insert(i,s[i])
                index.insert(i,i)
        value.reverse()
        char_list = list(s)
        print(value,index)
        for i in range(len(index)):
            char_list[index[i]]= value[i]

        return "".join(char_list) 
            