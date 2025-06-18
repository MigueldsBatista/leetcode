
"""
LeetCode 1071: Greatest Common Divisor of Strings - Optimized Solution

This is the optimal solution using mathematical GCD approach.

Key Insight:
If a string X divides both str1 and str2, then str1 + str2 must equal str2 + str1.
This is because if both strings are made of repetitions of the same substring,
the concatenation order shouldn't matter.

Algorithm Steps:
1. First check if str1 + str2 == str2 + str1 (necessary condition)
2. If not equal, no common divisor exists, return ""
3. If equal, the GCD length is the GCD of the lengths of both strings
4. Return the substring of that length from either string

Time Complexity: O(n + m) where n = len(str1), m = len(str2)
- String concatenation and comparison: O(n + m)
- GCD calculation: O(log(min(n, m)))

Space Complexity: O(n + m) for string concatenation

Example Walkthrough:
str1 = "ABABAB", str2 = "ABAB"
1. str1 + str2 = "ABABABABAB"
2. str2 + str1 = "ABABABABAB" 
3. They are equal, so a common divisor exists
4. gcd(6, 4) = 2
5. Return str2[:2] = "AB"
"""

from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Step 1: Check if both strings can be formed by repeating the same substring
        # If they can, then concatenating them in any order should give the same result
        if str1 + str2 != str2 + str1:
            return ""  # No common divisor exists
        
        # Step 2: Find the GCD of the lengths - this gives us the length of the 
        # greatest common divisor string
        gcd_length = gcd(len(str1), len(str2))
        
        # Step 3: Return the substring of that length (from either string)
        return str2[:gcd_length]


# Test the optimized solution
solution = Solution()

test_cases = [
    ("ABCABC", "ABC"),     # Expected: "ABC"
    ("ABABAB", "ABAB"),    # Expected: "AB" 
    ("LEET", "CODE"),      # Expected: ""
    ("AAAAAA", "AAA"),     # Expected: "AAA"
]

print("Testing optimized solution:")
for str1, str2 in test_cases:
    result = solution.gcdOfStrings(str1, str2)
    print(f"gcdOfStrings('{str1}', '{str2}') = '{result}'")