
"""
LeetCode 1768: Merge Strings Alternately - Inefficient Approach

Problem Description:
You are given two strings word1 and word2. Merge the strings by adding letters 
in alternating order, starting with word1. If a string is longer than the other, 
append the additional letters onto the end of the merged string.

Algorithm - Pop-based Approach (Inefficient):
1. Convert both strings to lists
2. Use pop(0) to remove first character from each string alternately
3. Continue until one string is empty
4. Append remaining characters from the non-empty string

Time Complexity: O(n²) where n is total length of both strings
- pop(0) operation on list is O(n) because it shifts all remaining elements
- We do this for each character, making it O(n²) overall

Space Complexity: O(n) for the converted lists and result

Why This Approach is Inefficient:
- pop(0) on a list requires shifting all remaining elements left by one position
- This makes each pop(0) operation O(n), leading to O(n²) overall complexity
- Converting strings to lists is unnecessary overhead

Example Walkthrough:
word1 = "abc", word2 = "pqr"

Initial: word1 = ['a','b','c'], word2 = ['p','q','r'], word3 = []

Iteration 1:
- pop(0) from word1 → 'a', word1 = ['b','c'] (O(n) operation!)
- pop(0) from word2 → 'p', word2 = ['q','r'] (O(n) operation!)
- word3 = ['a','p']

Iteration 2:
- pop(0) from word1 → 'b', word1 = ['c'] (O(n) operation!)
- pop(0) from word2 → 'q', word2 = ['r'] (O(n) operation!)
- word3 = ['a','p','b','q']

Iteration 3:
- pop(0) from word1 → 'c', word1 = [] (O(n) operation!)
- pop(0) from word2 → 'r', word2 = [] (O(n) operation!)
- word3 = ['a','p','b','q','c','r']

Result: "apbqcr"
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Step 1: Convert strings to lists (unnecessary overhead)
        word3 = list()
        word1 = list(word1)
        word2 = list(word2)

        # Step 2: Alternate between strings while both have characters
        # WARNING: pop(0) is O(n) operation - very inefficient!
        while word1 and word2:
            c1 = word1.pop(0)  # O(n) - shifts all remaining elements
            c2 = word2.pop(0)  # O(n) - shifts all remaining elements

            word3.append(c1)
            word3.append(c2)
        
        # Step 3: Append remaining characters from word1 if any
        while word1:
            c1 = word1.pop(0)  # Still O(n) operation
            word3.append(c1)
        
        # Step 4: Append remaining characters from word2 if any
        while word2:
            c2 = word2.pop(0)  # Still O(n) operation
            word3.append(c2)
        
        # Step 5: Join list into final string
        return "".join(word3)


# Test the inefficient solution
test_cases = [
    ("abc", "pqr"),        # Expected: "apbqcr"
    ("ab", "pqrs"),        # Expected: "apbqrs"  
    ("abcd", "pq"),        # Expected: "apbqcd"
    ("", "abc"),           # Expected: "abc"
    ("abc", ""),           # Expected: "abc"
]

print("Testing inefficient pop(0) approach:")
print("Note: This solution has O(n²) time complexity due to pop(0) operations")
print()

solution = Solution()

for word1, word2 in test_cases:
    result = solution.mergeAlternately(word1, word2)
    print(f"mergeAlternately('{word1}', '{word2}') = '{result}'")

print()
print("Performance Analysis:")
print("- Each pop(0) operation takes O(n) time")  
print("- With n total characters, we get O(n²) overall complexity")
print("- This approach is inefficient for large strings")
print("- See v2.py for the optimized O(n) solution")
