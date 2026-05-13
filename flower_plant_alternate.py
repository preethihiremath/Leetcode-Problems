# 605. Can Place Flowers
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # 0 is empty 1 is not empty
        # = true ==> if n flower can be planted no adjacent 

        # check if n slots are open i.e n slots are 0 
        # check if they can be placed non-adjacent

        #add virutal zeros
        flowerbed=[0]+flowerbed +[0]
        size=len(flowerbed)
        count=0
        for i in range(1, size -1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i]=1
                count+=1
        return count >=n
    
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        res=False
        prev=0
        nexts=0
        placed=n


        # MORE EFFICIENT

        # for i in range(len(flowerbed)):
        #     if flowerbed[i] == 0:
        #         # Check if left is empty OR we are at the start
        #         empty_left = (i == 0 or flowerbed[i-1] == 0)
        #         # Check if right is empty OR we are at the end
        #         empty_right = (i == len(flowerbed)-1 or flowerbed[i+1] == 0)
                
        #         if empty_left and empty_right:
        #             flowerbed[i] = 1
        #             placed -= 1

        for i in range(0,len(flowerbed)):
            nexts=i+1
            prev=i-1
            if len(flowerbed) == 1:
                if flowerbed[i] == 0:
                    flowerbed[i] = 1
                    placed -= 1
            if i == 0 and len(flowerbed) > 1:
                if(flowerbed[i] == 0) and (flowerbed[nexts] == 0):
                    flowerbed[i]=1
                    placed -=1
                
            elif i == len(flowerbed) -1:
                if(flowerbed[i] == 0) and (flowerbed[prev] == 0):
                    flowerbed[i]=1
                    placed -=1

            else:
                
                if(flowerbed[i] == 0) and (flowerbed[nexts] == 0) and (flowerbed[prev] == 0):
                    flowerbed[i]=1
                    placed -=1
        print(placed)
        if placed <= 0 :
            res= True

        return res
        