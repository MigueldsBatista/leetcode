"""
LeetCode 605: Can Place Flowers - Optimized Unified Approach

Algorithm - Single Loop with Boundary Checking:
This is a cleaner, more robust solution that handles all cases in a unified manner.

Key Insights:
1. For each empty position, check if both neighbors are empty (or don't exist)
2. Use boundary conditions: treat positions before start and after end as empty
3. Early termination: return True as soon as we can place n flowers

Boundary Handling:
- Left neighbor: empty if i == 0 OR flowerbed[i-1] == 0
- Right neighbor: empty if i == length-1 OR flowerbed[i+1] == 0

Time Complexity: O(n) where n is the length of flowerbed
Space Complexity: O(1) - only using constant extra space

Example Walkthrough:
flowerbed = [1,0,0,0,1], n = 1

i=0: flowerbed[0] = 1, skip
i=1: flowerbed[1] = 0
  - left_empty = (1 == 0) OR (flowerbed[0] == 0) = False OR False = False
  - Can't plant (adjacent to existing flower)
i=2: flowerbed[2] = 0  
  - left_empty = (2 == 0) OR (flowerbed[1] == 0) = False OR True = True
  - right_empty = (2 == 4) OR (flowerbed[3] == 0) = False OR True = True
  - Can plant! count = 1, flowerbed = [1,0,1,0,1]
  - count >= n (1), return True

This approach is much cleaner than handling cases separately!
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:        
        count = 0  # Count of flowers we can actually plant
        length = len(flowerbed)
        
        # Single loop through all positions
        for i in range(length):
            # Skip positions that already have flowers
            if flowerbed[i] == 1:
                continue
            
            # Check if left neighbor is empty (or doesn't exist)
            left_empty = (i == 0) or (flowerbed[i - 1] == 0)
            
            # Check if right neighbor is empty (or doesn't exist)  
            right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
            
            # If both neighbors are empty, we can place a flower
            if left_empty and right_empty:
                flowerbed[i] = 1  # Place the flower
                count += 1
                
                # Early termination: return as soon as we have enough flowers
                if count >= n:
                    return True
        
        # Check if we planted enough flowers
        return count >= n

# Test the optimized unified approach
test_cases = [
    ([1,0,0,0,1], 1),        # Expected: True
    ([1,0,0,0,1], 2),        # Expected: False
    ([0], 1),                # Expected: True
    ([1], 1),                # Expected: False
    ([0,0,1,0,0], 1),        # Expected: True
    ([1,0,1,0,0,1,0,0], 2),  # Expected: True
    ([0,0,0,0,0], 3),        # Expected: True (can plant at 0,2,4)
    ([1,0,0,0,0,1], 2),      # Expected: False (can only plant at 2)
]

print("Testing Can Place Flowers - Optimized Unified Approach:")
print("Time: O(n), Space: O(1) with early termination!")
print()

solution = Solution()

for flowerbed, n in test_cases:
    # Make a copy to avoid modifying original for display
    original = flowerbed.copy()
    result = solution.canPlaceFlowers(flowerbed, n)
    print(f"canPlaceFlowers({original}, {n}) = {result}")
    print(f"  After planting: {flowerbed}")
    
    # Show detailed walkthrough for first example
    if original == [1,0,0,0,1] and n == 1:
        print("  Detailed walkthrough:")
        temp_bed = original.copy()
        count = 0
        length = len(temp_bed)
        
        print(f"  Initial: {temp_bed}")
        
        for i in range(length):
            print(f"  i={i}: flowerbed[{i}] = {temp_bed[i]}")
            
            if temp_bed[i] == 1:
                print(f"    Position {i} has flower, skip")
                continue
                
            left_empty = (i == 0) or (temp_bed[i-1] == 0)
            right_empty = (i == length-1) or (temp_bed[i+1] == 0)
            
            print(f"    left_empty: {left_empty}, right_empty: {right_empty}")
            
            if left_empty and right_empty:
                temp_bed[i] = 1
                count += 1
                print(f"    Can plant! count={count}, bed: {temp_bed}")
                if count >= n:
                    print(f"    Reached target {n}, early return!")
                    break
            else:
                print(f"    Cannot plant (neighbors occupied)")
                
        print(f"  Final result: {count >= n}")
    print()

print("Advantages of v2 over v1:")
print("- Single unified loop handles all cases")
print("- Clean boundary checking with logical operators")
print("- Early termination for better performance")
print("- No separate case handling needed")
print("- More robust and less error-prone")