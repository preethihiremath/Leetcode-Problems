#  Unique Number of Occurrences
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
# Example 1:

# Input: arr = [1,2,2,1,1,3]
# Output: true# 

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dictt ={}
        for i in arr:
            if i in dictt:
                dictt[i]+=1
            else:
                dictt[i]=1
        dict_size=len(dictt)
        unique_val=len(set(dictt.values()))
        # means its unique 
        if dict_size == unique_val :
            return True
        else :
            return False
            
# More effiient solution using Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        # Check if the number of unique elements equals the number of unique counts
        return len(counts) == len(set(counts.values()))
    