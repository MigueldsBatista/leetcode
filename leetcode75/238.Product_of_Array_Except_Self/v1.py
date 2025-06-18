
"""
LeetCode 238: Product of Array Except Self - Prefix/Postfix Approach

Problem Description:
Given an integer array nums, return an array answer such that answer[i] 
is equal to the product of all the elements of nums except nums[i].

Constraints:
- Must run in O(n) time complexity
- Cannot use division operator
- Follow-up: Can you solve it with O(1) extra space complexity?

Algorithm - Two Arrays Approach:
This solution uses the concept of prefix and postfix products.

Key Insight:
For each index i, the result is: prefix_product[i-1] * postfix_product[i+1]
- prefix_product[i] = product of all elements before index i
- postfix_product[i] = product of all elements after index i

Example: [1, 2, 3, 4]
- prefix products: [1, 2, 6, 24] (cumulative product from left)
- postfix products: [24, 24, 12, 4] (cumulative product from right)

For result[i]:
- result[0] = postfix[1] = 24 (product of [2, 3, 4])
- result[1] = prefix[0] * postfix[2] = 1 * 12 = 12 (product of [1] * [3, 4])
- result[2] = prefix[1] * postfix[3] = 2 * 4 = 8 (product of [1, 2] * [4])
- result[3] = prefix[2] = 6 (product of [1, 2, 3])

Time Complexity: O(n) - three passes through the array
Space Complexity: O(n) - for prefix and postfix arrays

Note: This solution has some inefficiencies:
- Uses insert(0, x) which is O(n) operation, making postfix construction O(n²)
- Can be optimized to use O(1) extra space (see v2.py)
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Step 1: Build prefix products array
        # prefix[i] contains product of all elements from index 0 to i (inclusive)
        prefix = 1
        prefixes = []
        for i in range(len(nums)):
            if i == 0:
                prefix = nums[i]
                prefixes.append(prefix)
                continue

            prefix = prefix * nums[i]
            prefixes.append(prefix)

        # Step 2: Build postfix products array
        # postfix[i] contains product of all elements from index i to end (inclusive)
        # WARNING: insert(0, x) is O(n) operation, making this O(n²) overall!
        postfix = 1
        postfixes = []
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                postfix = nums[i]
                postfixes.insert(0, postfix)  # O(n) operation - inefficient!
                continue

            postfix = postfix * nums[i]
            postfixes.insert(0, postfix)  # O(n) operation - inefficient!
            
        # Step 3: Build result by combining prefix and postfix products
        # For each index, multiply the product before it with the product after it
        result = []
        for i in range(len(nums)):
            if i == 0:
                # First element: no elements before, so use postfix[i+1]
                result.append(postfixes[i + 1])
                continue
            
            if i == len(nums)-1:
                # Last element: no elements after, so use prefix[i-1]
                num = prefixes[i - 1]
                result.append(num)
                continue

            # Middle elements: multiply prefix before * postfix after
            num = prefixes[i - 1] * postfixes[i + 1]
            result.append(num)

        return result


# Test the solution with detailed walkthrough
test_cases = [
    [1, 2, 3, 4],         # Expected: [24, 12, 8, 6]
    [2, 3, 4, 5],         # Expected: [60, 40, 30, 24]
    [-1, 1, 0, -3, 3],    # Expected: [0, 0, 9, 0, 0]
]

print("Testing Product of Array Except Self - Two Arrays Approach:")
print("Note: This solution has O(n²) complexity due to insert(0) operations")
print()

solution = Solution()

for nums in test_cases:
    result = solution.productExceptSelf(nums)
    print(f"Input: {nums}")
    print(f"Output: {result}")
    
    # Show detailed walkthrough for first example
    if nums == [1, 2, 3, 4]:
        print("Detailed walkthrough:")
        
        # Show prefix calculation
        prefix = 1
        prefixes = []
        for i in range(len(nums)):
            if i == 0:
                prefix = nums[i]
            else:
                prefix = prefix * nums[i]
            prefixes.append(prefix)
        print(f"  Prefix products: {prefixes}")
        
        # Show postfix calculation (conceptually)
        postfix_products = [24, 24, 12, 4]  # What should be calculated
        print(f"  Postfix products: {postfix_products}")
        
        # Show result calculation
        print("  Result calculation:")
        for i in range(len(nums)):
            if i == 0:
                calc = f"postfix[{i+1}] = {postfix_products[i+1]}"
            elif i == len(nums)-1:
                calc = f"prefix[{i-1}] = {prefixes[i-1]}"
            else:
                calc = f"prefix[{i-1}] * postfix[{i+1}] = {prefixes[i-1]} * {postfix_products[i+1]} = {prefixes[i-1] * postfix_products[i+1]}"
            print(f"    result[{i}] = {calc}")
    print()