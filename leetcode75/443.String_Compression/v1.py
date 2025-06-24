# 443. String Compression
# Hint
# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.

# Example 1:

# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
# Example 2:

# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a single character.
# Example 3:

# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

"""
LeetCode 443: String Compression - In-Place Two-Pointer Approach

ALGORITHM EXPLANATION:
This problem asks to compress consecutive repeating characters in-place.
The format is: character + count (if count > 1), stored back in the same array.

IN-PLACE COMPRESSION TECHNIQUE:
Use two pointers:
- 'index' (read pointer): traverses the original array
- 'write' (write pointer): writes compressed result back to same array

STEP-BY-STEP ALGORITHM:
1. Handle edge case: single character array
2. Initialize read (index) and write pointers
3. For each group of consecutive characters:
   a. Count consecutive occurrences
   b. Write the character to write position
   c. If count > 1, write each digit of count
   d. Move to next different character
4. Return the new length (write position)

KEY INSIGHTS:
- Groups with count=1: only write the character
- Groups with count>1: write character + digits of count
- Multi-digit counts: write each digit separately
- In-place modification: write result back to input array

TIME COMPLEXITY: O(n) - single pass through array
SPACE COMPLEXITY: O(1) - only using constant extra space

EXAMPLE WALKTHROUGH:
chars = ["a","a","b","b","c","c","c"]

Step 1: index=0, char='a', count consecutive 'a's: count=2
- Write 'a' at chars[0], write=1
- Write '2' at chars[1], write=2
- index=2

Step 2: index=2, char='b', count consecutive 'b's: count=2  
- Write 'b' at chars[2], write=3
- Write '2' at chars[3], write=4
- index=4

Step 3: index=4, char='c', count consecutive 'c's: count=3
- Write 'c' at chars[4], write=5  
- Write '3' at chars[5], write=6
- index=7 (end)

Result: chars = ["a","2","b","2","c","3"], return 6

EDGE CASES:
- Single character: return 1
- No compression needed: each char appears once
- Large counts: multi-digit numbers split into separate chars
"""

# Practice recommendation: Revisit this problem to master in-place array compression techniques

class Solution:
    def compress(self, chars: list[str]) -> int:
        # Step 1: Handle edge case - single character array
        if len(chars) == 1:
            print(chars)
            return 1  # Fixed: should return length, not array
        
        # Step 2: Initialize two pointers for in-place compression
        write = 0    # Write pointer: where to write compressed result
        index = 0    # Read pointer: current position being processed
        
        # Step 3: Process each group of consecutive characters
        while index < len(chars):  # Fixed: simplified condition
            cont = 1  # Count of current character
            char = chars[index]  # Current character being processed
            
            # Step 4: Count consecutive occurrences of current character
            while index + 1 < len(chars) and char == chars[index + 1]:
                cont += 1    # Increment count for each duplicate
                index += 1   # Move to next duplicate character
            
            # Step 5: Write character to compressed position
            chars[write] = char
            write += 1
            
            # Step 6: Write count if greater than 1 (multi-digit handling)
            if cont > 1:
                # Convert count to string and write each digit separately
                for digit_char in str(cont):
                    chars[write] = digit_char
                    write += 1
            
            # Step 7: Move to next different character
            index += 1
        
        print(chars)
        return write  # Return new length of compressed array
    
chars = ["a","a","b","b","c","c","c"]
chars = ["a"]
chars = ["a","b","c"]
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

res = Solution().compress(chars)
