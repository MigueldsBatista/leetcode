


"""
LeetCode 1431: Kids With the Greatest Number of Candies - Optimized Solution

Algorithm - Approach 2 (Optimized with max):
1. Find the maximum number of candies any kid currently has
2. For each kid, check if their candies + extraCandies >= max_candies
3. This is equivalent to checking if candies[i] >= max_candies - extraCandies

Key Insight:
Instead of checking if kid[i] + extraCandies >= max(candies), we can rearrange to:
kid[i] >= max(candies) - extraCandies

This avoids recalculating the maximum for each kid.

Time Complexity: O(n) - one pass to find max, one pass to check each kid
Space Complexity: O(1) - only using constant extra space (excluding output)

Example Walkthrough:
candies = [2,3,5,1,3], extraCandies = 3
max_candies = 5

For each kid, check if candies[i] >= max_candies - extraCandies = 5 - 3 = 2:
- Kid 0: 2 >= 2 → True
- Kid 1: 3 >= 2 → True  
- Kid 2: 5 >= 2 → True
- Kid 3: 1 >= 2 → False
- Kid 4: 3 >= 2 → True

Result: [True, True, True, False, True]

Why this works:
If kid[i] + extraCandies >= max_candies, then kid[i] will have at least as many 
candies as the current maximum, making them tied for the greatest.
"""

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        # Step 1: Find the current maximum number of candies
        max_candie = max(candies)
        
        # Step 2: Check each kid using list comprehension
        # Kid i can have the greatest if: candies[i] + extraCandies >= max_candie
        # Rearranged: candies[i] >= max_candie - extraCandies
        return [i >= max_candie - extraCandies for i in candies]


# Test the optimized solution
test_cases = [
    ([2,3,5,1,3], 3),      # Expected: [True,True,True,False,True]
    ([4,2,1,1,2], 1),      # Expected: [True,False,False,False,False]
    ([12,1,12], 10),       # Expected: [True,False,True]
]

print("Testing optimized solution:")
solution = Solution()

for candies, extraCandies in test_cases:
    result = solution.kidsWithCandies(candies, extraCandies)
    max_candies = max(candies)
    threshold = max_candies - extraCandies
    
    print(f"candies={candies}, extraCandies={extraCandies}")
    print(f"max_candies={max_candies}, threshold={threshold}")
    print(f"Result: {result}")
    print()
    