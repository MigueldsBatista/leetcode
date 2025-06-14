        
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
        """
        Improved Solution:
        - Single loop with proper boundary checking
        - Early termination when n flowers are placed
        - O(n) time complexity, O(1) space complexity
        - No modification of original array needed
        """
        count = 0
        length = len(flowerbed)
        
        for i in range(length):
            # Check if current position is empty
            if flowerbed[i] == 1:
                continue
        
            # Check left neighbor (or assume empty if at start)
            left_empty = (i == 0) or (flowerbed[i - 1] == 0)
            # Check right neighbor (or assume empty if at end)
            right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
            
            # If both neighbors are empty, we can place a flower
            if left_empty and right_empty:
                flowerbed[i] = 1  # Place flower
                count += 1
                
                # Early termination optimization
                if count >= n:
                    return True
    
        return count >= n