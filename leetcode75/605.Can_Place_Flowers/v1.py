
"""
LeetCode 605: Can Place Flowers - Case-by-Case Approach

Problem Description:
You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
and an integer n, return True if n new flowers can be planted in the flowerbed without violating
the no-adjacent-flowers rule, and False otherwise.

Algorithm - Case-by-Case Analysis:
This solution handles different cases separately:
1. Single element array
2. First position (only check right neighbor)
3. Last position (only check left neighbor)  
4. Middle positions (check both neighbors)

Time Complexity: O(n) where n is the length of flowerbed
Space Complexity: O(1) - only using constant extra space

Example Walkthrough:
flowerbed = [1,0,0,0,1], n = 1

Case analysis:
- Position 0: flowerbed[0] = 1, can't plant
- Position 1: left=1, current=0, right=0 → can't plant (adjacent to 1)
- Position 2: left=0, current=0, right=0 → can plant! → flowerbed = [1,0,1,0,1]
- Position 3: left=1, current=0, right=1 → can't plant (adjacent to both)
- Position 4: flowerbed[4] = 1, can't plant

Total flowers planted: 1, n = 1 → True

Note: This solution has some bugs in the edge case handling.
The loop range and conditions need to be carefully managed to avoid index errors.
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        can = 0  # Count of flowers we can plant
        
        # Special case: single element array
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            flowerbed[0] = 1
            can += 1

        # Check if we can plant at the first position
        # Only need to check right neighbor (no left neighbor exists)
        if len(flowerbed) > 1 and flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            can += 1

        # Check if we can plant at the last position  
        # Only need to check left neighbor (no right neighbor exists)
        if len(flowerbed) > 1 and flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            can += 1
        
        # Check middle positions (indices 1 to len-2)
        # Need to check both left and right neighbors
        for i in range(1, len(flowerbed) - 1):
            # Check if current position is empty and both neighbors are empty
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1  # Plant flower
                can += 1
            
        # Return True if we can plant at least n flowers
        return can >= n
# Test the case-by-case approach
test_cases = [
    ([1,0,0,0,1], 1),        # Expected: True
    ([1,0,0,0,1], 2),        # Expected: False
    ([0], 1),                # Expected: True
    ([1], 1),                # Expected: False
    ([0,0,1,0,0], 1),        # Expected: True
    ([1,0,1,0,0,1,0,0], 2),  # Expected: True
]

print("Testing Can Place Flowers - Case-by-Case Approach:")
print("Note: This approach handles edge cases separately")
print()

solution = Solution()

for flowerbed, n in test_cases:
    # Make a copy to avoid modifying original for display
    original = flowerbed.copy()
    result = solution.canPlaceFlowers(flowerbed, n)
    print(f"canPlaceFlowers({original}, {n}) = {result}")
    print(f"  After planting: {flowerbed}")
    
    # Show step-by-step for first example
    if original == [1,0,0,0,1] and n == 1:
        print("  Step-by-step analysis:")
        temp_bed = original.copy()
        can_plant = 0
        
        print(f"  Initial: {temp_bed}")
        
        # Single element check
        if len(temp_bed) == 1 and temp_bed[0] == 0:
            print("  Single element case: can plant")
            can_plant += 1
        
        # First position
        if len(temp_bed) > 1 and temp_bed[0] == 0 and temp_bed[1] == 0:
            print("  First position: can plant")
            temp_bed[0] = 1
            can_plant += 1
            
        # Last position  
        if len(temp_bed) > 1 and temp_bed[-1] == 0 and temp_bed[-2] == 0:
            print("  Last position: can plant")
            temp_bed[-1] = 1
            can_plant += 1
            
        # Middle positions
        for i in range(1, len(temp_bed) - 1):
            if temp_bed[i-1] == 0 and temp_bed[i] == 0 and temp_bed[i+1] == 0:
                print(f"  Position {i}: can plant")
                temp_bed[i] = 1
                can_plant += 1
                
        print(f"  Total flowers planted: {can_plant}")
        print(f"  Final bed: {temp_bed}")
    print()

print("Issues with this approach:")
print("- Handles cases separately, making code complex")
print("- Some edge cases might have bugs")
print("- Loop range needs careful management")
print("- See v2.py for a cleaner unified approach")