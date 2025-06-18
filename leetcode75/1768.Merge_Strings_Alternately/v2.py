
"""
LeetCode 1768: Merge Strings Alternately - Optimized Solution

Algorithm - Index-based Approach (Efficient):
1. Use a single index to iterate through both strings simultaneously
2. Alternate adding characters from word1 and word2 while both have characters
3. Append remaining characters from the longer string using string slicing

Time Complexity: O(n) where n is the total length of both strings
- Single loop through the shorter string: O(min(len1, len2))
- String slicing for remaining characters: O(max(len1, len2) - min(len1, len2))
- Overall: O(len1 + len2) = O(n)

Space Complexity: O(n) for the result list

Key Improvements over v1:
- No pop(0) operations that cause O(n²) complexity
- Direct string indexing instead of converting to lists
- Single loop instead of multiple while loops
- String slicing to handle remaining characters efficiently

Example Walkthrough:
word1 = "abc", word2 = "pqr"

Initialization: result = [], i = 0

Iteration 1 (i=0):
- word1[0] = 'a', word2[0] = 'p'
- result = ['a', 'p']
- i = 1

Iteration 2 (i=1):
- word1[1] = 'b', word2[1] = 'q'
- result = ['a', 'p', 'b', 'q']
- i = 2

Iteration 3 (i=2):
- word1[2] = 'c', word2[2] = 'r'
- result = ['a', 'p', 'b', 'q', 'c', 'r']
- i = 3

End condition: i >= len(word1) and i >= len(word2)
- word1[3:] = "" (empty)
- word2[3:] = "" (empty)
- result = ['a', 'p', 'b', 'q', 'c', 'r', '', '']

Final result: "apbqcr"
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Step 1: Initialize result list and index pointer
        result = []
        i = 0

        # Step 2: Alternate between characters while both strings have characters
        # Continue until we reach the end of the shorter string
        while i < len(word1) and i < len(word2):
            result.append(word1[i])  # Add character from word1
            result.append(word2[i])  # Add character from word2
            i += 1
            
        # Step 3: Append remaining characters from longer string
        # One of these slices will be empty, the other contains remaining chars
        result.append(word1[i:])  # Remaining chars from word1 (if any)
        result.append(word2[i:])  # Remaining chars from word2 (if any)
        
        # Step 4: Join all parts into final string
        return "".join(result)

# Test the optimized solution
test_cases = [
    ("abc", "pqr"),        # Expected: "apbqcr"
    ("ab", "pqrs"),        # Expected: "apbqrs"  
    ("abcd", "pq"),        # Expected: "apbqcd"
    ("", "abc"),           # Expected: "abc"
    ("abc", ""),           # Expected: "abc"
]

print("Testing optimized index-based approach:")
print("Time Complexity: O(n) - much better than v1's O(n²)")
print()

solution = Solution()

for word1, word2 in test_cases:
    result = solution.mergeAlternately(word1, word2)
    print(f"mergeAlternately('{word1}', '{word2}') = '{result}'")
    
    # Show detailed steps for first example
    if word1 == "abc" and word2 == "pqr":
        print("  Step-by-step process:")
        i = 0
        temp_result = []
        while i < len(word1) and i < len(word2):
            temp_result.extend([word1[i], word2[i]])
            print(f"    i={i}: Added '{word1[i]}' and '{word2[i]}' → {temp_result}")
            i += 1
        remaining1 = word1[i:]
        remaining2 = word2[i:]
        if remaining1 or remaining2:
            print(f"    Remaining: '{remaining1}' + '{remaining2}'")
    print()

print("Comparison with v1:")
print("- v1 (pop approach): O(n²) time complexity")
print("- v2 (index approach): O(n) time complexity") 
print("- For large strings, v2 is significantly faster!")