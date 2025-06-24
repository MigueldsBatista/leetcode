"""
1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length

"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Step 1: Define vowels set for O(1) lookup
        vogals = set('aeiou')
        max_window = 0      # Maximum vowels found so far
        current_window = 0  # Vowels in current window

        # Step 2: Build initial window of size k
        for i in range(k):
            letter = s[i]
            if letter in vogals:
                current_window += 1

        # Step 3: Initialize max with first window
        max_window = current_window

        # Step 4: Slide the window across the remaining string
        for i in range(k, len(s)):
            letter = s[i]           # New character entering window
            left_slide = s[i - k]   # Character leaving window

            # Step 5: Remove element going out of window
            if left_slide in vogals:
                current_window -= 1

            # Step 6: Add element coming into window  
            if letter in vogals:
                current_window += 1

            # Step 7: Update maximum vowels found
            max_window = max(current_window, max_window)

        return max_window




s = "abciiidef"
k = 3
# Output: 3

# s = "aeiou"
# k = 2
# # Output: 2

# s = "leetcode"
# k = 3

# # Output: 2

# s = "weallloveyou"
# k = 7

# Output: 4

res = Solution().maxVowels(s, k)
print(res)

"""
LeetCode 1456: Maximum Number of Vowels in a Substring of Given Length - Sliding Window

ALGORITHM EXPLANATION:
This problem asks for the maximum number of vowels in any substring of length k.
The optimal approach is to use the sliding window technique.

SLIDING WINDOW APPROACH:
Instead of checking every possible substring of length k (which would be O(n*k)),
we can slide a window of size k across the string and update the vowel count efficiently.

STEP-BY-STEP ALGORITHM:
1. Build the initial window of size k and count vowels in it
2. Slide the window one position at a time:
   - Remove the leftmost character from window
   - Add the new rightmost character to window  
   - Update vowel count accordingly
3. Keep track of maximum vowel count seen

KEY INSIGHT:
When sliding the window, we only need to check:
- The character leaving the window (subtract if it's a vowel)
- The character entering the window (add if it's a vowel)

TIME COMPLEXITY: O(n) - single pass through string
SPACE COMPLEXITY: O(1) - only using constant extra space

EXAMPLE WALKTHROUGH:
s = "abciiidef", k = 3

Step 1: Build initial window "abc"
- vowel count = 1 ('a')
- max_window = 1

Step 2: Slide to "bci" 
- remove 'a' (vowel): count = 0
- add 'i' (vowel): count = 1
- max_window = max(1, 1) = 1

Step 3: Slide to "cii"
- remove 'b' (not vowel): count = 1  
- add 'i' (vowel): count = 2
- max_window = max(1, 2) = 2

Step 4: Slide to "iii"
- remove 'c' (not vowel): count = 2
- add 'i' (vowel): count = 3
- max_window = max(2, 3) = 3

Continue sliding... Final answer: 3
"""