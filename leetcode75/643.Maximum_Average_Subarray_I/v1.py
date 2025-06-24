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
This problem requires finding the maximum average of any contiguous subarray of length k.
We use the SLIDING WINDOW technique for optimal O(n) solution.

SLIDING WINDOW APPROACH:
Instead of calculating sum for each subarray from scratch (O(n*k)),
we maintain a running sum and slide the window efficiently.

STEP-BY-STEP ALGORITHM:
1. Handle edge case: if k equals array length, return average of entire array
2. Initialize variables: index, running total, max average
3. Expand window: add elements until window size reaches k
4. Slide window: for each subsequent position:
   a. Add new element entering window
   b. Remove element leaving window 
   c. Calculate current average and update maximum
5. Return the maximum average found

KEY INSIGHTS:
- Only need to track sums, not individual elements
- Sliding window avoids redundant calculations
- First window (size k) establishes initial maximum
- Each slide: +1 new element, -1 old element

TIME COMPLEXITY: O(n) - single pass through array
SPACE COMPLEXITY: O(1) - only using constant extra space

EXAMPLE WALKTHROUGH:
nums = [1,12,-5,-6,50,3], k = 4

Step 1: Build first window (i=0 to 3)
- i=0: total = 1
- i=1: total = 1+12 = 13  
- i=2: total = 13+(-5) = 8
- i=3: total = 8+(-6) = 2, maxAverage = 2/4 = 0.5

Step 2: Slide window (i=4 onwards)
- i=4: total = 2+50-1 = 51, maxAverage = max(0.5, 51/4) = 12.75
- i=5: total = 51+3-12 = 42, maxAverage = max(12.75, 42/4) = 12.75

Result: 12.75
"""


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Step 1: Handle edge case - window size equals array length
        if k == len(nums):
            return sum(nums)/k
        
        # Step 2: Initialize variables for sliding window
        i = 0              # Current index in array
        total = 0          # Running sum of current window
        maxAverage = 0     # Maximum average found so far
        
        # Step 3: Process each element with sliding window technique
        while i < len(nums):
            num = nums[i]
            total += num   # Add current element to window sum
            
            # Step 4: First complete window of size k
            if i == k - 1:
                maxAverage = total/k  # Set initial maximum average
            
            # Step 5: Slide window for subsequent elements
            elif i >= k:
                total -= nums[i - k]  # Remove element leaving window
                # Update maximum with current window's average
                maxAverage = max(total/k, maxAverage)
            
            i += 1
        
        return maxAverage


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