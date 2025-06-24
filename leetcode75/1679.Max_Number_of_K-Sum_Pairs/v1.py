"""
1679. Max Number of K-Sum Pairs
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.

"""

class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        """
        LeetCode 1679: Max Number of K-Sum Pairs - Two Pointers Approach

        ALGORITHM EXPLANATION:
        This problem asks to find the maximum number of pairs that sum to k.
        We use the TWO POINTERS technique after sorting the array.

        TWO POINTERS ON SORTED ARRAY:
        After sorting, use two pointers from opposite ends:
        - If sum < k: need larger sum, move left pointer right
        - If sum > k: need smaller sum, move right pointer left  
        - If sum == k: found valid pair, move both pointers

        STEP-BY-STEP ALGORITHM:
        1. Sort the array to enable two-pointer technique
        2. Initialize left=0 (start), right=n-1 (end), count=0
        3. While left < right:
           a. Calculate sum of elements at both pointers
           b. If sum equals k: increment count, move both pointers
           c. If sum less than k: move left pointer right (increase sum)
           d. If sum greater than k: move right pointer left (decrease sum)
        4. Return total count of pairs found

        KEY INSIGHTS:
        - Sorting enables efficient two-pointer traversal
        - Each element used at most once (pointers don't cross back)
        - Greedy approach: always move towards target sum
        - No need to track actual pairs, just count them

        TIME COMPLEXITY: O(n log n) - dominated by sorting step
        SPACE COMPLEXITY: O(1) - only using constant extra space (excluding sort space)

        EXAMPLE WALKTHROUGH:
        nums = [1,2,3,4], k = 5
        
        Step 1: Sort array → [1,2,3,4] (already sorted)
        Step 2: left=0, right=3, count=0
        
        Step 3: Process pairs
        - nums[0] + nums[3] = 1 + 4 = 5 == k → count=1, left=1, right=2
        - nums[1] + nums[2] = 2 + 3 = 5 == k → count=2, left=2, right=1
        - left >= right → stop
        
        Result: 2 operations possible

        EDGE CASES:
        - Array with less than 2 elements: return 0
        - No valid pairs exist: return 0
        - All elements form pairs: return n/2
        - Duplicate elements: handled correctly by pointer movement
        """
        # Step 1: Sort array to enable two-pointer technique
        nums.sort()
        
        # Step 2: Initialize two pointers and counter
        left = 0                    # Start pointer
        right = len(nums) - 1       # End pointer  
        count = 0                   # Count of valid pairs
        
        # Step 3: Use two pointers to find pairs summing to k
        while left < right:
            sum_val = nums[left] + nums[right]  # Current pair sum
            
            # Step 4: Adjust pointers based on sum comparison
            if sum_val == k:
                count += 1      # Found valid pair
                left += 1       # Move left pointer right
                right -= 1      # Move right pointer left
            elif sum_val < k:
                left += 1       # Need larger sum, move left right
            else:
                right -= 1      # Need smaller sum, move right left
        
        return count

nums = [3,1,3,4,3]
k = 6