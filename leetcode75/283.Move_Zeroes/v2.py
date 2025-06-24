"""
283. Move Zeroes - Optimized One-Pass Solution

APPROACH 2: Single-Pass with Smart Swapping
1. Use write pointer to track position for next non-zero element
2. When we find non-zero, swap it with element at write position
3. Only swap when write_pos != current_pos (optimization)

TIME COMPLEXITY: O(n) - single pass
SPACE COMPLEXITY: O(1) - constant extra space
OPERATIONS: Minimized swaps compared to two-pass approach

STEP-BY-STEP EXAMPLE:
Input: [0,1,0,3,12]
i=0, write=0: nums[0]=0 (skip, write stays 0)
i=1, write=0: nums[1]=1 (swap with nums[0]) -> [1,0,0,3,12], write=1
i=2, write=1: nums[2]=0 (skip, write stays 1)  
i=3, write=1: nums[3]=3 (swap with nums[1]) -> [1,3,0,0,12], write=2
i=4, write=2: nums[4]=12 (swap with nums[2]) -> [1,3,12,0,0], write=3
"""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Optimal one-pass solution with minimal swaps
        """
        # Step 1: Initialize write pointer for next non-zero position
        write_pos = 0  # Position where next non-zero should go
        
        # Step 2: Single pass through array
        for i in range(len(nums)):
            if nums[i] != 0:
                # Step 3: Found non-zero element, place it at write position
                # Only swap if positions are different (optimization)
                if i != write_pos:
                    nums[write_pos], nums[i] = nums[i], nums[write_pos]
                    
                # Step 4: Move write pointer forward
                write_pos += 1
        
        print(f"Result: {nums}")

# Test with detailed trace
def test_with_trace():
    solution = Solution()
    nums = [0,1,0,3,12]
    print(f"Original: {nums}")
    
    # Manual trace to show the process
    write_pos = 0
    for i in range(len(nums)):
        print(f"Step {i+1}: i={i}, write_pos={write_pos}, nums[{i}]={nums[i]}")
        if nums[i] != 0:
            if i != write_pos:
                nums[write_pos], nums[i] = nums[i], nums[write_pos]
                print(f"  Swapped: {nums}")
            write_pos += 1
        else:
            print(f"  Zero found, skip")
        print(f"  Current array: {nums}")
        print()
    
    print(f"Final result: {nums}")

test_with_trace()