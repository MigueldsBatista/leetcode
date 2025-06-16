"""
LeetCode 605: Can Place Flowers

Problem Description:
You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
and an integer n, return True if n new flowers can be planted in the flowerbed without violating
the no-adjacent-flowers rule, and False otherwise.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False

Constraints:
- 1 <= flowerbed.length <= 2 * 10^4
- flowerbed[i] is 0 or 1
- There are no two adjacent flowers in flowerbed
- 0 <= n <= flowerbed.length
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        
        can = 0
        #caso aonde a lista só tem 1 elemento
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            flowerbed[0] = 1
            can+=1

        #caso onde n é o primeiro da lista
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            can+=1

        #caso onde n é o último da lista
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            can+=1
        
        for i in range(len(flowerbed)-1):

            #caso onde n está no meio da lista
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                can+=1
            
        return can >= n
        
flowerbed = [1,0,0,0,1,0,0]

n = 2
can = Solution().canPlaceFlowers(flowerbed, n)
print(can)