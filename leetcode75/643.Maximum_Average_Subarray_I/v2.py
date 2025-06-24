"""
643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000

ALGORITHM EXPLANATION:
This is an OPTIMIZED SLIDING WINDOW approach that tracks maximum sum instead of maximum average.
Key insight: Since all subarrays have the same length k, maximizing sum is equivalent to maximizing average.

OPTIMIZED SLIDING WINDOW TECHNIQUE:
1. Build the first window sum
2. Slide window and track maximum sum (not average)
3. Convert to average only at the end

STEP-BY-STEP ALGORITHM:
1. Handle edge cases:
   - If k equals array length: return average of entire array
   - If k equals 1: return maximum single element
2. Build first window: calculate sum of first k elements
3. Initialize max_sum with first window sum
4. Slide window through remaining elements:
   - Remove leftmost element, add rightmost element
   - Update maximum sum if current sum is larger
5. Return max_sum divided by k for final average

KEY OPTIMIZATION:
- Track maximum sum instead of maximum average
- Only one division operation at the end
- Avoids floating-point arithmetic during comparison

TIME COMPLEXITY: O(n) - single pass through array after initial window
SPACE COMPLEXITY: O(1) - only using constant extra space

EXAMPLE WALKTHROUGH:
nums = [1,12,-5,-6,50,3], k = 4

Step 1: Build first window sum
- total = 1 + 12 + (-5) + (-6) = 2
- max_sum = 2

Step 2: Slide window
- i=4: total = 2 - 1 + 50 = 51, max_sum = max(2, 51) = 51
- i=5: total = 51 - 12 + 3 = 42, max_sum = max(51, 42) = 51

Step 3: Return average
- max_sum/k = 51/4 = 12.75

PERFORMANCE COMPARISON:
- This approach avoids repeated division operations
- More numerically stable than comparing floating-point averages
- Cleaner separation of window logic and final calculation
"""


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Step 1: Handle edge case - window size equals array length
        if k == len(nums):
            return sum(nums)/k
        
        # Step 2: Handle edge case - single element windows
        if k == 1:
            return max(nums)  # Maximum single element
        
        # Step 3: Build first window sum
        total = 0
        for i in range(k):
            total += nums[i]  # Sum first k elements
        max_sum = total       # Initialize maximum sum
        
        # Step 4: Slide window through remaining elements
        for i in range(k, len(nums)):
            # Slide window: remove left element, add right element
            total = total - nums[i - k] + nums[i]
            # Update maximum sum if current window sum is larger
            max_sum = max(max_sum, total)
        
        # Step 5: Convert maximum sum to maximum average
        # Key insight: max sum corresponds to max average since k is constant
        return max_sum/k


nums = [1,12,-5,-6,50,3]
k = 4

nums = [5]
k = 1

nums = [4,0,4,3,3]
k = 5

nums = [9,7,3,5,6,2,0,8,1,9]
k = 6

from test_case import nums

k = 6514
#-25.14477

res = Solution().findMaxAverage(nums, k)
print(res)