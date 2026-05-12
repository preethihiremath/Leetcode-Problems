# 283. Move Zeroes
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        non_zero_idx = 0
    
    # Iterate through the array and move non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                # If the current element is non-zero, swap it with the element at non_zero_idx
                # and increment non_zero_idx
                nums[i], nums[non_zero_idx] = nums[non_zero_idx], nums[i]
                non_zero_idx += 1

        return nums
        
        


            

        