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

    """
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        #step 1: build prefix:
        prefix = 1
        prefixes = []
        for i in range(len(nums)):
            if i == 0:
                prefix = nums[i]
                prefixes.append(prefix)
                continue

            prefix = prefix * nums[i]
            prefixes.append(prefix)

        #step 2: build postfixes
        postfix = 1
        postfixes = []
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                postfix = nums[i]
                postfixes.insert(0, postfix)
                continue

            postfix = postfix * nums[i]
            postfixes.insert(0, postfix)
            
        #step 3: build result
        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(postfixes[i + 1])
                continue
            
            if i == len(nums)-1:
                num = prefixes[i - 1]
                result.append(num)
                continue

            num = prefixes[i - 1] * postfixes[i + 1]
            result.append(num)

        return result
    
nums = [1, 2, 3, 4]
Solution().productExceptSelf(nums)