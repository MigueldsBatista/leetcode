class Solution:
    def isValid(self, s: str) -> bool:
        
        match = {
            '{':'}',
            '[':']',
            '(':')'
        }
        opening = set('({[')
        stack = []
        
        if len(s) % 2 != 0:
            return False

        for symbol in s:
            if symbol in opening:
                stack.append(symbol)
                continue

            if len(stack) == 0:
                return False
                
            candidate = stack.pop()
                
            if match.get(candidate) != symbol:
                return False
                
        return not stack

s = "([}}])".replace()
# s = "()"

res = Solution().isValid(s)
print(res)