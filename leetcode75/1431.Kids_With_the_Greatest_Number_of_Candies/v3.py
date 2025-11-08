
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        # Step 1: Initialize result array
        output = []
        max_candies = max(candies)
        for i in range(len(candies)):
            kid_candies = candies[i] + extraCandies
            if kid_candies >= max_candies:
                output.append(True)
                continue
            output.append(False)
            
        return output