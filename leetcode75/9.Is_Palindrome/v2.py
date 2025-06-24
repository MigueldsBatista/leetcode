class Solution:
    def isPalindrome(self, x: int) -> bool:
        return x == x[::-1]
    
print(Solution().isPalindrome(313))