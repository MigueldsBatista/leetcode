"""
LeetCode Problem 345: Reverse Vowels of a String

This solution reverses only the vowels in a given string while keeping 
consonants in their original positions.

Algorithm:
1. Create a set of vowels (both lowercase and uppercase)
2. Extract all vowels from the string in order
3. Reverse the list of vowels
4. Replace vowels in the original string with reversed vowels

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(n) for storing the vowels and converting string to list

Example:
Input: "IceCreAm" 
Output: "AceCreIm"
(vowels I,e,e,A are reversed to A,e,e,I)
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')

        word_vowels = []
        s = list(s)
        for letter in s:
            if letter in vowels:
                word_vowels.append(letter)

        word_vowels = word_vowels[::-1]
        for index, letter in enumerate(s):
            if letter in vowels:
                s[index] = word_vowels.pop(0)
                
                # We could also use the string approach
                # s = s[:index] + word_vowels.pop(0) + s[index + 1:]
        
        return ''.join(s)

res = Solution().reverseVowels('IceCreAm')
print(res)