# Single Number
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bins =0
        for i in range(0,len(nums)):
            bins=bins^nums[i]

        return bins