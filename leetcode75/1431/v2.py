

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candie = max(candies)
        return [i >= max_candie - extraCandies for i in candies]
    