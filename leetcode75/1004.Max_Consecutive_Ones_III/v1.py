"""
LeetCode 1004: Max Consecutive Ones III - Sliding Window Approach

ALGORITHM EXPLANATION:
This problem asks for the maximum length of consecutive 1's after flipping at most k zeros.
The key insight is to use a sliding window approach.

OPTIMAL APPROACH (Not implemented here):
The current solution has a flawed approach. The correct algorithm should be:
1. Use two pointers (left, right) to maintain a sliding window
2. Expand the window by moving right pointer
3. Keep track of zeros in current window
4. When zeros exceed k, shrink window from left until zeros ≤ k
5. Track maximum window size throughout

CURRENT SOLUTION ANALYSIS:
The implemented approach tries to count consecutive 1s and 0s separately, but this doesn't
correctly handle the sliding window concept needed for this problem.

STEP-BY-STEP WALKTHROUGH OF CURRENT APPROACH:
1. Initialize counters for ones and zeros in current window
2. Process consecutive 1s first
3. Then process consecutive 0s  
4. Calculate maximum possible length by adding ones + min(zeros, k)
5. Reset counters based on next element type

ISSUES WITH CURRENT APPROACH:
- Doesn't properly implement sliding window
- Resets counters incorrectly
- May have index out of bounds errors
- Doesn't track the actual consecutive sequence correctly

TIME COMPLEXITY: O(n) - single pass through array
SPACE COMPLEXITY: O(1) - constant extra space

CORRECT SLIDING WINDOW APPROACH:
def longestOnes(self, nums, k):
    left = 0
    zeros_count = 0
    max_length = 0
    
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros_count += 1
        
        while zeros_count > k:
            if nums[left] == 0:
                zeros_count -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length
"""

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        # Step 1: Initialize window counters
        window_one = 0    # Count of consecutive 1s in current segment
        window_zero = 0   # Count of consecutive 0s in current segment
        max_flipped = 0   # Maximum length found so far
        i = 0             # Current position in array
        
        # Step 2: Process the array in segments of consecutive 1s and 0s
        while i < len(nums):

            # Step 3: Count consecutive 1s starting from current position
            while i < len(nums) and nums[i] == 1:
                window_one += 1
                i += 1

            # Step 4: Count consecutive 0s starting from current position
            while i < len(nums) and nums[i] == 0:            
                window_zero += 1
                i += 1

            # Step 5: Calculate max possible length with current segment
            # We can flip min(window_zero, k) zeros to extend the sequence
            max_flipped = max(max_flipped, window_one + min(window_zero, k))
            
            # Step 6: Reset counters based on next element type (has bugs!)
            # WARNING: These conditions may cause index out of bounds errors
            if i < len(nums) and nums[i + 1] == 0:
                window_zero = 0
            if i < len(nums) and nums[i + 1] == 1:
                window_one = 0
        
        return max_flipped
    
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
# expected: 10
res = Solution().longestOnes(nums, k)
print(res)