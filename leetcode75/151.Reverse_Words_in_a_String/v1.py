
"""
LeetCode 151: Reverse Words in a String

Problem Description:
Given an input string s, reverse the order of the words.
- A word is defined as a sequence of non-space characters
- Words are separated by at least one space
- Return words in reverse order, separated by single spaces
- Remove leading/trailing spaces and reduce multiple spaces to single space

Algorithm - Split and Filter Approach:
1. Split the string by spaces to get individual words
2. Filter out empty strings (caused by multiple consecutive spaces)  
3. Reverse the list of words
4. Join with single spaces

Time Complexity: O(n) where n is the length of the string
- split(): O(n)
- filter(): O(k) where k is number of parts after split
- reverse slice: O(k)  
- join(): O(n)

Space Complexity: O(n) for storing the split words

Example Walkthrough:
Input: "a good   example"

Step 1: s.split(' ') 
→ ['a', 'good', '', '', 'example']

Step 2: Filter out empty strings
→ ['a', 'good', 'example']

Step 3: Reverse the list ([::-1])
→ ['example', 'good', 'a']

Step 4: Join with single spaces
→ "example good a"

Edge Cases Handled:
- Leading/trailing spaces: "  hello world  " → "world hello"
- Multiple spaces: "a   b" → "b a"  
- Single word: "hello" → "hello"
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Split string by spaces to get all parts
        # This creates a list where empty strings represent multiple consecutive spaces
        parts = s.split(' ')
        
        # Step 2: Filter out empty strings caused by multiple spaces
        # Using lambda function to keep only non-empty parts
        if '' in parts:
            parts = list(filter(lambda x: x != '', parts))
        
        # Step 3: Reverse the list and join with single spaces
        # [::-1] reverses the list, ' '.join() combines with single spaces
        return ' '.join(parts[::-1])
    
# Test the solution
test_cases = [
    "a good   example",      # Expected: "example good a"
    "the sky is blue",       # Expected: "blue is sky the"
    "  hello world  ",       # Expected: "world hello"
    "hello",                 # Expected: "hello"
    "   a   b   c   ",      # Expected: "c b a"
]

print("Testing Reverse Words solution:")
solution = Solution()

for test_string in test_cases:
    result = solution.reverseWords(test_string)
    print(f"Input: '{test_string}' → Output: '{result}'")
    
    # Show the step-by-step process for first example
    if test_string == "a good   example":
        print("  Step-by-step:")
        parts = test_string.split(' ')
        print(f"  1. split(' '): {parts}")
        filtered = list(filter(lambda x: x != '', parts))
        print(f"  2. filter empty: {filtered}")
        reversed_parts = filtered[::-1]
        print(f"  3. reverse: {reversed_parts}")
        final = ' '.join(reversed_parts)
        print(f"  4. join: '{final}'")
    print()