"""
LeetCode 392: Is Subsequence - Two Pointer Approach

ALGORITHM EXPLANATION:
This problem asks to determine if string s is a subsequence of string t.
A subsequence maintains the relative order but allows gaps between characters.

TWO POINTER TECHNIQUE:
Use one pointer for each string:
- 'read' pointer tracks position in string s (what we're looking for)
- 'i' pointer tracks position in string t (where we're searching)

STEP-BY-STEP ALGORITHM:
1. Initialize read pointer at 0 for string s
2. Iterate through each character in string t
3. If current characters match: advance read pointer
4. If read pointer reaches end of s: found complete subsequence
5. Continue until we've processed all of t

KEY INSIGHT:
We only advance the 'read' pointer when we find a match, ensuring we maintain
the relative order of characters in s.

TIME COMPLEXITY: O(n) where n = len(t) - single pass through t
SPACE COMPLEXITY: O(1) - only using constant extra space

EXAMPLE WALKTHROUGH:
s = "abc", t = "ahbgdc"

Step 1: read=0, i=0, t[0]='a', s[0]='a' → MATCH! read=1
Step 2: read=1, i=1, t[1]='h', s[1]='b' → no match
Step 3: read=1, i=2, t[2]='b', s[1]='b' → MATCH! read=2  
Step 4: read=2, i=3, t[3]='g', s[2]='c' → no match
Step 5: read=2, i=4, t[4]='d', s[2]='c' → no match
Step 6: read=2, i=5, t[5]='c', s[2]='c' → MATCH! read=3

Final: read=3, len(s)=3 → read == len(s) → TRUE

EDGE CASES:
- Empty s: always true (empty subsequence)
- Empty t: true only if s is also empty
- s longer than t: impossible to be subsequence
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Step 1: Initialize read pointer for string s
        read = 0  # Tracks which character in s we're looking for
        
        # Step 2: Iterate through each character in string t
        for i in range(len(t)):
            # Step 3: Check if current characters match
            if read < len(s) and s[read] == t[i]:
                # Step 4: Found match! Move to next character in s
                read += 1
                
        # Step 5: Check if we found all characters of s
        # If read == len(s), we found complete subsequence
        return read == len(s)


s = "abc"
t = "ahbgdc"
# Output: true

print(Solution().isSubsequence(s, t))

s = "axc"
t = "ahbgdc"
# Output: false
print(Solution().isSubsequence(s, t))

s = "abc"

t = "ahbgdc"

# Output: true
print(Solution().isSubsequence(s, t))

s = "acb"
t = "ahbgdc"
# Output: false

res = Solution().isSubsequence(s, t)
print(res)