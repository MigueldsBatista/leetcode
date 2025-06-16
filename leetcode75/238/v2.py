class Solution:
    """
    Calculates the product of all elements in the array except the element at each index.

    This approach iterates through each position in the array, temporarily removes the element
    at that position, calculates the product of the remaining elements using reduce, then
    restores the element back to its original position. The product is stored in the result array.

    Note: This approach is not efficient due to the repeated use of expensive built-in operations
    like pop() and insert() which have O(n) time complexity, and reduce() which also takes O(n).
    The overall time complexity becomes O(n²), making it suboptimal for large arrays.

    -> Important points are that we need a solution of O(n) and we cant use the division operator
    since we could just multiply all nums and divide by the nth number

    The ideia here will be to imagine two arrays of prefix ad postfix numbers
    take for example [1, 2, 3, 4]
    if we multiply all numbers by the numbers before we will have a array of prefixes
    -> [1, 2, 6, 24]
    for example, 6 represents the product of all numbers before and the number at that index
    
    When we think of the postfix array we go backwards
    [4] -> [12, 4] -> [24, 12, 4] -> [24, 24, 12, 4]
    same is valid here, if we think of 12 it represents the product of all numbers after if
    and the number at  that index

    After this process we would have two arrays
    prefix = [1, 2, 6, 24]
    postfix = [24, 24, 12, 4]
    Meaning that it we want to know the value of a number at a certain index, we just need
    to multiply the number before and the number after it

    NEETCODE: https://www.youtube.com/watch?v=bNvIQI2wAjk

    #TODO -> come here again to try this problem again
    """
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        result = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        print(result)
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result

nums = [1, 2, 3, 4]
nums = [-1,1,0,-3,3]
Solution().productExceptSelf(nums)