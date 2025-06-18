
"""
LeetCode 1071: Greatest Common Divisor of Strings

Problem Description:
For two strings s and t, we say "t divides s" if s = t + ... + t 
(i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Approach:
This is a brute force approach that checks all possible substrings of str1 to see 
if they can divide both strings.

Algorithm Steps:
1. Iterate through all possible substrings of str1 (from length 1 to full length)
2. For each substring, check if it can divide both str1 and str2
3. A string divides another if splitting by that string results in empty parts only
4. Keep track of the longest valid divisor found

Time Complexity: O(n * (n + m)) where n = len(str1), m = len(str2)
- O(n) iterations for each substring
- O(n + m) for split operations and join operations

Space Complexity: O(n + m) for storing split results

Note: This solution has a bug - it doesn't handle the case correctly where 
str1="ABABAB" and str2="ABAB" should return "AB", not "ABAB".
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Step 1: Initialize candidate to store the best divisor found so far
        candidate = ''
        
        # Step 2: Try all possible substrings of str1 as potential divisors
        for index in range(len(str1)):
            # Step 3: Extract substring from start to current index
            substr = str1[:index+1]
            
            # Step 4: Test if this substring can divide both strings
            # Split both strings by the substring - if it's a valid divisor,
            # all parts should be empty strings
            temp = str2.split(substr)    # Split str2 by current substring
            temp2 = str1.split(substr)   # Split str1 by current substring
            
            # Step 5: Check if both strings are completely divisible
            # If join of split parts is empty, the substring divides the string
            if ''.join(temp) == '' and ''.join(temp2) == '':
                candidate = str1[:index+1]  # Update candidate with longer divisor
                
        # Step 6: Return the longest valid divisor found
        return candidate

# Example walkthrough:
# str1 = "ABABAB", str2 = "ABAB"
# 
# Iteration 1: substr = "A"
# - str2.split("A") = ["", "B", "B"]  ->  join = "BB" != ""
# - Not a valid divisor
#
# Iteration 2: substr = "AB" 
# - str2.split("AB") = ["", "", ""]  ->  join = "" 
# - str1.split("AB") = ["", "", "", ""]  ->  join = ""
# - Valid divisor! candidate = "AB"
#
# Continue checking longer substrings...
# The algorithm should find "AB" as the GCD, but has a bug in implementation

# Test the solution
string = 'ABABAB'
solution = Solution().gcdOfStrings('ABABAB', 'ABAB')
print(f"Result: {solution}")
print(f"Expected: AB")

# Additional test cases:
test_cases = [
    ("ABCABC", "ABC"),     # Expected: "ABC"
    ("ABABAB", "ABAB"),    # Expected: "AB" 
    ("LEET", "CODE"),      # Expected: ""
]

for str1, str2 in test_cases:
    result = Solution().gcdOfStrings(str1, str2)
    print(f"gcdOfStrings('{str1}', '{str2}') = '{result}'")


