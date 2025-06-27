"""
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.

Oq eu pensei até agora, pegamos a menor palavra
e vamos ordenar nosso array de strings por tamanho
ou seja começamos a partir da segunda palavra
vamos vendo os prefixo e comparando a palavra com a nossa menor, pq ele vai ser o maior prefixo possível
se os números forem diferentes, vamos cortando até onde ainda for válido, mas como?
como otimizar o algoritmo tb, só imagino soluções n^2

TODO: go over this again

"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        prefix = strs[0]

        for string in strs[1:]:
            i = 0
            while i < len(prefix) and i < len(string) and prefix[i] == string[i]:
                i += 1

            prefix = prefix[:i]

            if not prefix:
                break

        return prefix


strs = ["dog", "racecar", "car"]

res = Solution().longestCommonPrefix(strs)
print(res)
