"""
LeetCode 1: Two Sum - Hash Map Approach

ALGORITHM EXPLANATION:
This solution uses a hash map (dictionary) to solve the Two Sum problem in a single pass.

The key insight is that for each number, we can calculate its complement (target - current_number) 
and check if we've seen this complement before in our traversal.

STEP-BY-STEP ALGORITHM:
1. Initialize an empty hash map to store {number: index} pairs
2. Iterate through the array with both value and index
3. For each element, calculate its complement: complement = target - current_number
4. Check if the complement exists in our hash map
5. If found: return [complement_index, current_index] 
6. If not found: store current number and its index in hash map
7. Continue until solution is found

TIME COMPLEXITY: O(n) - single pass through the array
SPACE COMPLEXITY: O(n) - hash map can store up to n elements

EXAMPLE WALKTHROUGH:
nums = [2,7,11,15], target = 9

Step 1: i=0, num=2, complement=9-2=7
- Check if 7 in num_map: NO
- Store: num_map = {2: 0}

Step 2: i=1, num=7, complement=9-7=2  
- Check if 2 in num_map: YES (at index 0)
- Return [0, 1]

Why this works:
- We're looking for two numbers that sum to target
- If current number is 'a', we need 'b' where a + b = target, so b = target - a
- Hash map gives us O(1) lookup to find if we've seen 'b' before
- By storing indices, we can return the positions when found

ADVANTAGES:
- Single pass solution (optimal)
- Uses hash map for O(1) lookups
- Handles duplicate values correctly
- Space-time tradeoff: uses more space but much faster than brute force O(n²)
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Step 1: Initialize hash map to store {number: index} pairs
        num_map = dict()
        
        # Step 2: Iterate through array with index
        for i in range(len(nums)):
            num = nums[i]
            
            # Step 3: Calculate complement needed to reach target
            complement = target - num
            
            # Step 4: Check if complement was seen before
            candidate = num_map.get(complement)
            if candidate is not None:
                # Step 5: Found pair! Return indices [earlier_index, current_index]
                return [candidate, i]
            
            # Step 6: Store current number and its index for future lookups
            num_map[num] = i


# Test cases with detailed walkthrough
test_cases = [
    ([2,7,11,15], 9),      # Expected: [0,1]
    ([3,2,4], 6),          # Expected: [1,2] 
    ([3,3], 6),            # Expected: [0,1]
    ([1,2,3,4,5], 8),      # Expected: [2,4]
]

print("Testing Two Sum - Hash Map Approach:")
print("Time: O(n), Space: O(n)")
print()

solution = Solution()

for nums, target in test_cases:
    result = solution.twoSum(nums, target)
    print(f"twoSum({nums}, {target}) = {result}")
    
    # Verify result
    if result:
        sum_check = nums[result[0]] + nums[result[1]]
        print(f"  Verification: nums[{result[0]}] + nums[{result[1]}] = {nums[result[0]]} + {nums[result[1]]} = {sum_check}")
        print(f"  ✅ Correct!" if sum_check == target else f"  ❌ Wrong!")
    print()

# Show detailed trace for first example
print("Detailed trace for [2,7,11,15], target=9:")
nums = [2,7,11,15]
target = 9
num_map = {}

for i in range(len(nums)):
    num = nums[i]
    complement = target - num
    print(f"Step {i+1}: num={num}, complement={complement}")
    
    if complement in num_map:
        print(f"  Found complement {complement} at index {num_map[complement]}")
        print(f"  Return [{num_map[complement]}, {i}]")
        break
    else:
        num_map[num] = i
        print(f"  Store {num} at index {i}")
        print(f"  num_map = {num_map}")
    print()