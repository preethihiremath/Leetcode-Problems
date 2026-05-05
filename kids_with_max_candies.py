# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

# Return a boolean array result of length n, where resleafult[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

# Note that multiple kids can have the greatest number of candies.

 

# Example 1:

# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true] 

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
         curr_max= max(candies)
         res=list()

         for i in range (0,len(candies)):

            new_val = candies[i] + extraCandies 
            print(new_val)
            if new_val >= curr_max:
                res.append(True)
            else: 
                res.append(False)
            # if new_val > curr_max:
            #     curr_max=new_val

         return res

