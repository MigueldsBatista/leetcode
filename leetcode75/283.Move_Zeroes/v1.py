#TODO repeat this problem   
"""
283. Move Zeroes

PROBLEM: Move all zeros to the end while maintaining relative order of non-zero elements.

APPROACH 1: Two-Pass Solution
1. First pass: Move all non-zero elements to the front
2. Second pass: Fill remaining positions with zeros

TIME COMPLEXITY: O(n) - two passes through array
SPACE COMPLEXITY: O(1) - only using constant extra space

STEP-BY-STEP EXAMPLE:
Input: [0,1,0,3,12]
Pass 1 - Move non-zeros: [1,3,12,3,12] (write_pos = 3)
Pass 2 - Fill zeros: [1,3,12,0,0]
"""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Step 1: Initialize pointers
        i = 0       # Read pointer - traverses the entire array
        write = 0   # Write pointer - position for next non-zero element
        
        # Step 2: First pass - move all non-zero elements to front
        while i < len(nums):
            num = nums[i]
            if num != 0:
                # Found non-zero element, place it at write position
                nums[write] = nums[i]
                write += 1  # Move write pointer forward
                i += 1
                continue
               
            # Skip zeros in first pass
            i += 1
            
        # Step 3: Second pass - fill remaining positions with zeros
        for i in range(write, len(nums)):
            nums[i] = 0


nums = [0,1,0,3,12]
# nums = [0, 1]
Solution().moveZeroes(nums)