"""
Increasing Triplet Subsequence - Algorithm Explanation

This solution maintains only TWO values:
- first: smallest number seen so far
- second: smallest number greater than first seen so far

Strategy:
1. If we find a number ≤ first → update first
2. If we find a number > first but ≤ second → update second
3. If we find a number > second → we have our triplet!

Key Insight:
Even if first or second get updated later, what matters is that at some point
we had a valid sequence. The algorithm maintains minimal candidates to maximize
the chances of forming a valid increasing triplet. And we know for a fact
that if a value is bigger than the second its also bigger than the first
we could say that this function makes good use of transisive functions

Example: [20, 100, 10, 12, 5, 13]
- After processing: first=5, second=12
- When we see 13: we have 5 < 12 < 13 ✓

Common Misconception:
The numbers don't need to be consecutive in the array, and updating first
doesn't invalidate previous valid sequences.

"""


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        # Keep track of the smallest and second smallest numbers seen so far

        # NOTE: float('inf') -> represents an infinite positive value

        for num in nums:
            if first is None or num <= first:
                first = num  # Update smallest
                continue

            if second is None or num <= second:
                second = num  # Update second smallest
                continue

            # Found a number greater than both first and second
            return True  # We have our triplet: first < second < num

        return False


arrays = [
    # [5, 4, 3, 2, 1],
    # [2,1,5,0,4,6],
    [20, 100, 10, 12, 5, 13],
    # [1,5,0,4,1,3],
    # [2,5,3,4,5],
    # [5,1,5,5,2,5,4],
    # [2,4,-2,-3],
    # [1,1,-2,6],
    # [1,0,-1,0,100000000]
]

print(f"Result: {Solution().increasingTriplet(arrays[0])}")
