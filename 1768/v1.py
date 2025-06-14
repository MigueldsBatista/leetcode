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
        word3 = list()
        word1 = list(word1)
        word2 = list(word2)

        while word1 and word2:
            c1 = word1.pop(0)
            c2 = word2.pop(0)

            word3.append(c1)
            word3.append(c2)
        
        while word1:
            c1 = word1.pop(0)
            word3.append(c1)
        
        while word2:
            c2 = word2.pop(0)
            word3.append(c2)
        
        return "".join(word3)


word = Solution().mergeAlternately("abc", "pqr")  # Output: "apbqcr"
print(word)

res = filter(lambda x, y: x > y, [1, 2, 3, 4, 5])

print(res)
