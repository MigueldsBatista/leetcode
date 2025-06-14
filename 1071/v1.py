class Solution:
    """
    Find the largest string that divides both str1 and str2.
    
    A string X divides string Y if Y can be constructed by concatenating
    copies of X. This method finds the greatest common divisor (GCD) of
    two strings by checking all possible substrings of str1 to see if
    they can divide both input strings.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The largest string that divides both str1 and str2.
             Returns empty string if no such divisor exists.
    
    Example:
        >>> solution = Solution()
        >>> solution.gcdOfStrings("ABCABC", "ABC")
        "ABC"
        >>> solution.gcdOfStrings("ABABAB", "ABAB")
        "AB"
        >>> solution.gcdOfStrings("LEET", "CODE")
        ""
    """
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        candidate = ''
        for index in range(len(str1)):
            substr = str1[:index+1]
            temp = str2.split(substr)
            temp2 = str1.split(substr)
            if ''.join(temp) == '' and ''.join(temp2) == '':
                candidate = str1[:index+1]
        return candidate

string = 'ABABAB'
solution = Solution().gcdOfStrings('ABABAB', 'ABAB')
print(solution)

# str1 "ABABAB"
# str2 "ABAB"
# Output "ABAB"
# Expected "AB"


