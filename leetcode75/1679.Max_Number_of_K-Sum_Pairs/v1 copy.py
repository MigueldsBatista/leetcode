"""
1679. Max Number of K-Sum Pairs
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.

TODO: refazer esssa sol e dps fazer uma com two pointers

"""

class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        num_count = {}
        cont = 0
        for num in nums:
            complement = (k - num)
            if complement in num_count and num_count[complement] > 0:
                cont += 1
                num_count[complement] -= 1
                continue
            
            num_count[num] = num_count.get(num, 0) + 1

        return cont

nums = [3,1,3,4,3]
k = 6

nums = [1,2,3,4]
k = 5

nums = [3,1,5,1,1,1,1,1,2,2,3,2,2]
k = 1

nums = [2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2]
k = 3
res = Solution().maxOperations(nums, k)
print(res)