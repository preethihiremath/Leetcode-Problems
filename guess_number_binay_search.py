# 374. Guess Number Higher or Lower
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).

# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

# You call a pre-defined API int guess(int num), which returns three possible results:

# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def getVal(self,i,n):
            print("start and end",i,n)
            mid = int((i+n)/2)  # interger division to get the mid value  also can be done as (i+n)//2
            print("mid",mid)
            g = guess(mid)
            print("guess",g)
            if (g == 0):
                return mid
            if (g == -1):
                return self.getVal(i,mid-1)
            if (g == 1):
                return self.getVal(mid+1, n)
        
    def guessNumber(self, n: int) -> int:
            i=1
            if i == n: 
                return n
            g = self.getVal(i,n)
            print("final value",g)
            return g
        