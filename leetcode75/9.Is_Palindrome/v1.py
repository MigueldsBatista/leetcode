class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        org = x
        if x < 0:
            return False
        
        while x:
            mod = x % 10
            x = x // 10
            rev = rev * 10 + mod

        return org == rev

print(Solution().isPalindrome(313))