
"""
LeetCode 345: Reverse Vowels of a String - Extract and Replace Approach

Problem Description:
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', 'u', and they can appear in both lower and upper cases.

Algorithm - Extract and Replace Approach:
1. Create a set of vowels for O(1) lookup (both lowercase and uppercase)
2. Extract all vowels from the string in the order they appear
3. Reverse the list of extracted vowels
4. Iterate through the string again, replacing each vowel with the next reversed vowel

Time Complexity: O(n) where n is the length of the string
- First pass to extract vowels: O(n)
- Reverse vowels list: O(v) where v is number of vowels
- Second pass to replace vowels: O(n)
- Overall: O(n)

Space Complexity: O(n) 
- Converting string to list: O(n)
- Storing vowels: O(v) where v ≤ n

Example Walkthrough:
Input: "IceCreAm"

Step 1: Extract vowels
- vowels found: ['I', 'e', 'e', 'A']

Step 2: Reverse vowels
- reversed: ['A', 'e', 'e', 'I']  

Step 3: Replace in original string
- I → A: "AceCreAm"
- e → e: "AceCreAm" 
- e → e: "AceCreAm"
- A → I: "AceCreIm"

Result: "AceCreIm"

Note: This approach uses pop(0) which is O(n) operation, making it suboptimal.
See v2.py for a more efficient two-pointer approach.
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        # Step 1: Define vowels set for O(1) lookup
        vowels = set('aeiouAEIOU')

        # Step 2: Extract all vowels from the string
        word_vowels = []
        s = list(s)  # Convert to list for mutability
        for letter in s:
            if letter in vowels:
                word_vowels.append(letter)

        # Step 3: Reverse the vowels list
        word_vowels = word_vowels[::-1]
        
        # Step 4: Replace vowels in original string with reversed vowels
        for index, letter in enumerate(s):
            if letter in vowels:
                # WARNING: pop(0) is O(n) operation - inefficient!
                s[index] = word_vowels.pop(0)
                
                # Alternative string slicing approach (commented out):
                # s = s[:index] + word_vowels.pop(0) + s[index + 1:]
        
        # Step 5: Convert back to string
        return ''.join(s)

# Test the extract and replace approach
test_cases = [
    "IceCreAm",            # Expected: "AceCreIm"
    "leetcode",            # Expected: "leotcede"
    "aA",                  # Expected: "Aa"
    "hello",               # Expected: "holle"
    "bcdfg",               # Expected: "bcdfg" (no vowels)
]

print("Testing Reverse Vowels - Extract and Replace Approach:")
print("Note: Uses pop(0) which makes some operations O(n²)")
print()

solution = Solution()

for test_string in test_cases:
    result = solution.reverseVowels(test_string)
    print(f"reverseVowels('{test_string}') = '{result}'")
    
    # Show step-by-step for first example
    if test_string == "IceCreAm":
        print("  Step-by-step process:")
        vowels_set = set('aeiouAEIOU')
        found_vowels = [c for c in test_string if c in vowels_set]
        print(f"  1. Extract vowels: {found_vowels}")
        reversed_vowels = found_vowels[::-1]
        print(f"  2. Reverse vowels: {reversed_vowels}")
        print(f"  3. Replace in original: '{test_string}' → '{result}'")
    print()

print("Performance Analysis:")
print("- Extract vowels: O(n)")
print("- Reverse vowels: O(v) where v = number of vowels")  
print("- Replace vowels: O(n * v) due to pop(0) operations")
print("- Overall: O(n * v) - can be improved to O(n)")
print("- See v2.py for optimized two-pointer approach")