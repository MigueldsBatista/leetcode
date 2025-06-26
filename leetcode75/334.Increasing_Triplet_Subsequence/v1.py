"""
334. Increasing Triplet Subsequence
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

TODO: good problem to solve periodically


"""
sets = []
sets.index()

class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        # Step 1: Initialize tracking variables
        first = None   # Smallest element seen so far
        second = None  # Smallest element larger than 'first'
        
        # Step 2: Iterate through array
        for num in nums:
            # Step 3: Update first if we found smaller or equal element
            if first is None or num <= first:
                first = num
                continue

            # Step 4: Update second if we found element between first and second
            if second is None or num <= second:
                second = num
                continue
                
            # Step 5: Found element larger than second - we have triplet!
            # At this point: first < second < num
            return True
        
        # Step 6: No triplet found
        return False
    

nums = [1,2,3,4,5]
res = Solution().increasingTriplet(nums)
print(res)

"""
LeetCode 334: Increasing Triplet Subsequence - Greedy Two-Variable Approach

ALGORITHM EXPLANATION:
This problem asks to find if there exists a triplet (i,j,k) where i < j < k and 
nums[i] < nums[j] < nums[k]. The challenge is to solve it in O(n) time and O(1) space.

KEY INSIGHT:
We don't need to track the actual indices, just whether such a pattern exists.
Use two variables to track the smallest and second smallest values seen so far.

GREEDY APPROACH:
1. Keep track of the smallest element (first)
2. Keep track of the smallest element that's larger than 'first' (second)  
3. If we find any element larger than 'second', we have our triplet

STEP-BY-STEP ALGORITHM:
1. Initialize first = None, second = None
2. For each number in array:
   - If num ≤ first: update first (always keep the smallest)
   - Else if num ≤ second: update second (smallest among larger than first)
   - Else: found triplet! (num > second > first)

WHY THIS WORKS:
- 'first' represents the smallest element seen so far
- 'second' represents the smallest element that's larger than some previous 'first'
- When we find num > second, we know there was a previous first < second < num

TIME COMPLEXITY: O(n) - single pass through array
SPACE COMPLEXITY: O(1) - only using two variables

EXAMPLE WALKTHROUGH:
nums = [2,1,5,0,4,6]

Step 1: num=2, first=None → first=2
Step 2: num=1, 1≤2 → first=1  
Step 3: num=5, 5>1 and second=None → second=5
Step 4: num=0, 0≤1 → first=0
Step 5: num=4, 4>0 and 4≤5 → second=4
Step 6: num=6, 6>4 → FOUND! (triplet: 0<4<6)

TRICKY PART:
Even though we updated 'first' to 0 after setting second=5, the algorithm still works
because when we found second=5, there was a previous first=1, so the pattern 1<5 existed.
When we later find 6>4, we have 0<4<6 as a valid triplet.
"""