
"""
LeetCode 345: Reverse Vowels of a String - Optimized Two-Pointer Approach

Algorithm - Two-Pointer Technique:
This is the optimal solution using two pointers to swap vowels in-place.

Key Insight:
Instead of extracting vowels and then replacing them, we can use two pointers
to find vowels from both ends and swap them directly.

Steps:
1. Convert string to list for mutability
2. Use two pointers: left starts at beginning, right starts at end
3. Move left pointer forward until it finds a vowel
4. Move right pointer backward until it finds a vowel  
5. Swap the vowels at both pointers
6. Continue until pointers meet

Time Complexity: O(n) - single pass through the string
Space Complexity: O(n) - for converting string to list

Example Walkthrough:
Input: "IceCreAm"
s = ['I', 'c', 'e', 'C', 'r', 'e', 'A', 'm']

Initial: i=0, j=7
- s[0]='I' is vowel, s[7]='m' is not vowel
- Move j left: j=6, s[6]='A' is vowel
- Swap: s[0] ↔ s[6] → ['A', 'c', 'e', 'C', 'r', 'e', 'I', 'm']
- Move pointers: i=1, j=5

Next: i=1, j=5  
- s[1]='c' is not vowel, move i right: i=2
- s[2]='e' is vowel, s[5]='e' is vowel
- Swap: s[2] ↔ s[5] → ['A', 'c', 'e', 'C', 'r', 'e', 'I', 'm'] (no change)
- Move pointers: i=3, j=4

Next: i=3, j=4
- i >= j, stop

Result: "AceCreIm"

This approach is much more efficient than v1!
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        # Step 1: Define vowels set for O(1) lookup
        vowels = set('aeiouAEIOU')
        
        # Step 2: Initialize two pointers
        i = 0                    # Left pointer
        j = len(s) - 1          # Right pointer
        s = list(s)             # Convert to list for mutability

        # Step 3: Use two pointers to find and swap vowels
        while i < j:
            # Move left pointer forward until we find a vowel
            while i < j and s[i] not in vowels:
                i += 1
                
            # Move right pointer backward until we find a vowel
            while i < j and s[j] not in vowels:
                j -= 1
                
            # Swap the vowels at both pointers
            s[i], s[j] = s[j], s[i]
            
            # Move both pointers toward the center
            i += 1
            j -= 1

        # Step 4: Convert back to string
        return ''.join(s)


# Test the optimized two-pointer approach
test_cases = [
    "IceCreAm",            # Expected: "AceCreIm"
    "leetcode",            # Expected: "leotcede"
    "aA",                  # Expected: "Aa"
    "hello",               # Expected: "holle"
    "bcdfg",               # Expected: "bcdfg" (no vowels)
    "aeiou",               # Expected: "uoiea"
]

print("Testing Reverse Vowels - Optimized Two-Pointer Approach:")
print("Time: O(n), Space: O(n) - much better than v1!")
print()

solution = Solution()

for test_string in test_cases:
    result = solution.reverseVowels(test_string)
    print(f"reverseVowels('{test_string}') = '{result}'")
    
    # Show detailed walkthrough for first example
    if test_string == "IceCreAm":
        print("  Detailed two-pointer walkthrough:")
        vowels_set = set('aeiouAEIOU')
        s_list = list(test_string)
        i, j = 0, len(s_list) - 1
        step = 1
        
        print(f"  Initial: {s_list}, i={i}, j={j}")
        
        while i < j:
            # Find left vowel
            while i < j and s_list[i] not in vowels_set:
                i += 1
            # Find right vowel  
            while i < j and s_list[j] not in vowels_set:
                j -= 1
            
            if i < j:
                print(f"  Step {step}: Found vowels '{s_list[i]}' at {i}, '{s_list[j]}' at {j}")
                s_list[i], s_list[j] = s_list[j], s_list[i]
                print(f"  After swap: {s_list}")
                i += 1
                j -= 1
                step += 1
        
        print(f"  Final result: {''.join(s_list)}")
    print()

print("Algorithm Comparison:")
print("- v1 (extract/replace): O(n * v) time due to pop(0) operations")
print("- v2 (two-pointer): O(n) time with single pass")
print("- v2 is the preferred approach for interviews!")