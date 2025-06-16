class Solution:
    """
    LeetCode 1768: Merge Strings Alternately

    Problem:
    You are given two strings word1 and word2. Merge the strings by adding letters 
    in alternating order, starting with word1. If a string is longer than the other, 
    append the additional letters onto the end of the merged string.

    Original Solution Issues:
    - Using pop(0) on lists is O(n) operation, making overall complexity O(n²)
    - Converting strings to lists unnecessarily
    - Multiple loops when one would suffice

    Improved Solution:
    - Use index-based iteration for O(n) time complexity
    - Single loop to handle alternating merge
    - Direct string operations
    """
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i = 0

        while i < len(word1) and i < len(word2):
            result.append(word1[i])
            result.append(word2[i])
            i+=1
            
        result.append(word1[i:])
        result.append(word2[i:])
        return "".join(result)

# Test the solution
word = Solution().mergeAlternately("abc", "pqr")  # Output: "apbqcr"
print(word)