
"""
LeetCode 238: Product of Array Except Self - Optimized O(1) Space Solution

This is the optimal solution that meets the follow-up requirement of O(1) extra space.

Algorithm - Single Array with Two Passes:
Instead of creating separate prefix and postfix arrays, we use the result array itself
to store intermediate values, reducing space complexity to O(1).

Key Insight:
1. First pass: Store prefix products in the result array
2. Second pass: Multiply each element by postfix products calculated on-the-fly

Example Walkthrough: [1, 2, 3, 4]

First Pass (Prefix products):
- result[0] = 1 (no elements before index 0)
- result[1] = 1 (product of elements before index 1: just 1)
- result[2] = 1*2 = 2 (product of elements before index 2: 1*2)
- result[3] = 1*2*3 = 6 (product of elements before index 3: 1*2*3)
Result after first pass: [1, 1, 2, 6]

Second Pass (Multiply by postfix):
- postfix starts as 1
- i=3: result[3] *= postfix (1) → result[3] = 6*1 = 6, postfix = 1*4 = 4
- i=2: result[2] *= postfix (4) → result[2] = 2*4 = 8, postfix = 4*3 = 12  
- i=1: result[1] *= postfix (12) → result[1] = 1*12 = 12, postfix = 12*2 = 24
- i=0: result[0] *= postfix (24) → result[0] = 1*24 = 24, postfix = 24*1 = 24

Final result: [24, 12, 8, 6]

Time Complexity: O(n) - two passes through the array
Space Complexity: O(1) - only using constant extra space (excluding output array)

This solution is optimal and meets all the problem constraints!
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Step 1: Initialize result array with all 1s
        result = [1] * (len(nums))
        
        # Step 2: First pass - fill result with prefix products
        # result[i] will contain the product of all elements before index i
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix          # Store current prefix product
            prefix *= nums[i]           # Update prefix for next iteration
        
        # At this point: result = [1, 1, 2, 6] for input [1, 2, 3, 4]
        
        # Step 3: Second pass - multiply by postfix products
        # Traverse backwards, maintaining postfix product and multiplying result
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix        # Multiply by postfix product
            postfix *= nums[i]          # Update postfix for next iteration
            
        return result

# Test the optimized solution
test_cases = [
    [1, 2, 3, 4],         # Expected: [24, 12, 8, 6]
    [2, 3, 4, 5],         # Expected: [60, 40, 30, 24]
    [-1, 1, 0, -3, 3],    # Expected: [0, 0, 9, 0, 0]
]

print("Testing Product of Array Except Self - Optimized O(1) Space Solution:")
print("Time: O(n), Space: O(1) - meets all constraints!")
print()

solution = Solution()

for nums in test_cases:
    result = solution.productExceptSelf(nums)
    print(f"Input: {nums}")
    print(f"Output: {result}")
    
    # Show step-by-step for first example
    if nums == [1, 2, 3, 4]:
        print("Step-by-step walkthrough:")
        
        # Simulate first pass
        temp_result = [1] * len(nums)
        prefix = 1
        print("  First pass (prefix products):")
        for i in range(len(nums)):
            temp_result[i] = prefix
            print(f"    result[{i}] = {prefix}")
            prefix *= nums[i]
        print(f"  After first pass: {temp_result}")
        
        # Simulate second pass
        postfix = 1
        print("  Second pass (multiply by postfix):")
        for i in range(len(nums)-1, -1, -1):
            old_val = temp_result[i]
            temp_result[i] *= postfix
            print(f"    result[{i}] = {old_val} * {postfix} = {temp_result[i]}")
            postfix *= nums[i]
        print(f"  Final result: {temp_result}")
    print()

print("Algorithm Comparison:")
print("- v1: O(n) time, O(n) space, but has O(n²) operations due to insert(0)")
print("- v2: O(n) time, O(1) space - optimal solution!")
print("- v2 is the preferred approach for interviews")