# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.

 

# Example 1:

# Input: nums1 = [1,2,3], nums2 = [2,4,6]
# Output: [[1,3],[4,6]]

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l1 =set()
        l2 =set()
        
        for i in range(0,len(nums1)):
            if nums1[i] not in nums2:
                l1.add(nums1[i])
        
           
        for i in range(0,len(nums2)):
            if nums2[i] not in nums1:
                l2.add(nums2[i])
        
        ans=[]
        ans.append(list(l1))
        ans.append(list(l2))
        return ans


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Convert both to sets: O(n + m)
        s1, s2 = set(nums1), set(nums2)
        
        # Use set difference to find unique elements: O(n + m)
        return [list(s1 - s2), list(s2 - s1)]
