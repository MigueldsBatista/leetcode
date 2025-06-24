"""
LeetCode 11: Container With Most Water - Brute Force Approach

ALGORITHM EXPLANATION:
This problem asks to find two lines that form a container holding the maximum water.
This implementation uses a BRUTE FORCE approach by checking all possible pairs.

BRUTE FORCE TECHNIQUE:
Check every possible pair of lines and calculate the water area for each.
The area is determined by: min(height[i], height[j]) * distance(i, j)

STEP-BY-STEP ALGORITHM:
1. Initialize max_area = 0
2. For each line i from 0 to n-1:
   a. For each line j from 0 to n-1:
      - Calculate area = min(height[i], height[j]) * |j - i|
      - Update max_area if current area is larger
3. Return the maximum area found

CRITICAL ISSUES WITH THIS IMPLEMENTATION:
1. REDUNDANT CALCULATIONS: Checks (i,j) and (j,i) separately - same result
2. ZERO-DISTANCE PAIRS: When i==j, distance=0, so area=0 (waste of computation)
3. INEFFICIENT: O(n²) when O(n) solution exists with two pointers

TIME COMPLEXITY: O(n²) - nested loops check all pairs
SPACE COMPLEXITY: O(1) - only using constant extra space

OPTIMIZATION OPPORTUNITIES:
1. Skip when i == j (distance = 0)
2. Use j > i to avoid duplicate calculations  
3. Better approach: Two pointers from ends (O(n) solution)

EXAMPLE WALKTHROUGH:
height = [1,8,6,2,5,4,8,3,7]

Brute force checks all 81 pairs:
- (0,1): min(1,8) * |1-0| = 1 * 1 = 1
- (0,2): min(1,6) * |2-0| = 1 * 2 = 2
- ...
- (1,8): min(8,7) * |8-1| = 7 * 7 = 49 ← maximum
- ...

Result: 49 (but with 81 calculations instead of optimal 9)

PERFORMANCE ANALYSIS:
- Finds correct answer but very inefficiently
- For large inputs, this will be too slow
- Two-pointer approach would be much better
"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Step 1: Initialize maximum area tracker
        maxArea = 0
        
        # Step 2: Check all possible pairs of lines (brute force)
        for i in range(len(height)):
            for j in range(len(height)):
                # Step 3: Calculate area for current pair
                # Area = min height × distance between lines
                area = min(height[i], height[j]) * abs(j - i)
                
                # Step 4: Update maximum if current area is larger
                if area > maxArea:
                    maxArea = area
        
        return maxArea