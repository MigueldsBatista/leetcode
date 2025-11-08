
"""
LeetCode 1431: Kids With the Greatest Number of Candies

Problem Description:
There are n kids with candies. Given an integer array candies where candies[i] 
represents the number of candies the ith kid has, and an integer extraCandies 
denoting the number of extra candies you have.

Return a boolean array result of length n, where result[i] is true if, after 
giving the ith kid all the extraCandies, they will have the greatest number 
of candies among all the kids, or false otherwise.

Note: Multiple kids can have the greatest number of candies.

Algorithm - Approach 1 (Using filter):
1. For each kid, calculate their total candies if given all extra candies
2. Use filter to check if any other kid has more candies than this total
3. If no kid has more, this kid can have the greatest number

Time Complexity: O(n²) - for each kid, we filter through all kids
Space Complexity: O(n) - for the output array and temporary filtered lists

Example Walkthrough:
candies = [2,3,5,1,3], extraCandies = 3

Kid 0: 2 + 3 = 5 candies
- Check if any kid has > 5: kid 2 has 5, but not > 5
- Result: True

Kid 1: 3 + 3 = 6 candies  
- Check if any kid has > 6: no kid has > 6
- Result: True

Kid 2: 5 + 3 = 8 candies
- Check if any kid has > 8: no kid has > 8  
- Result: True

Kid 3: 1 + 3 = 4 candies
- Check if any kid has > 4: kids 0,1,2,4 all have > 4
- Result: False

Kid 4: 3 + 3 = 6 candies
- Check if any kid has > 6: no kid has > 6
- Result: True

Final Output: [True, True, True, False, True]

#TODO X find a better solution than using filter because its expansive

"""

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        # Step 1: Initialize result array
        output = []
        
        # Step 2: Check each kid individually
        for i in range(len(candies)):
            # Step 3: Calculate total candies if this kid gets all extra candies
            temp = candies[i] + extraCandies
            
            # Step 4: Filter to find kids with more candies than this total
            # Using lambda function to check if any kid has more than temp
            filtered = filter(lambda kidCount: kidCount > temp, candies)
            
            # Step 5: If no kid has more candies, this kid can have the greatest
            if not list(filtered):  # Convert filter object to list to check if empty
                output.append(True)
                continue
            output.append(False)
            
        return output
    
# Test the solution
test_cases = [
    ([2,3,5,1,3], 3),      # Expected: [True,True,True,False,True]
    ([4,2,1,1,2], 1),      # Expected: [True,False,False,False,False]
    ([12,1,12], 10),       # Expected: [True,False,True]
]

print("Testing solution with filter approach:")
solution = Solution()

for candies, extraCandies in test_cases:
    result = solution.kidsWithCandies(candies, extraCandies)
    print(f"candies={candies}, extraCandies={extraCandies}")
    print(f"Result: {result}")
    print()
