"""

1004. Max Consecutive Ones III
Given a binary array nums and an integer k, 
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

"""
from typing import List
"""
sobre a solução, qual seria a lógica aq, nós temos um array binário
precisamos apenas de alguns artificios para construri a nossa solução
1. vamos precisar de dois ponteiros left e right que vão ser inicializados no início
do array, e o ponteiro direito serve para aumentar o tamanho da janela e o esquerdo para diminuir !
2. quando aumentarmos o tamanho da nossa janela precisamos verificar se ela é valida, para isso
basta ver se o número de zeros na janela atual <= k, e o número total de 1s seria o tamanho da janela
3. se chegarmos num ponto aonde nossa janela seja invalidada, precisamos mover o ponteiro esquerdo
até que o número de zeros volte a ficar balanceado

TODO - fazer dnv e entender melhor
"""

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_w = 0
        left = 0
        num_zeros = 0

        for right in range(len(nums)):

            if  nums[right] == 0:
                num_zeros += 1
            
            while num_zeros > k:
                if nums[left] == 0:
                    num_zeros -= 1
                left += 1

            max_w = max(max_w, right - left + 1)

        return max_w

res = Solution().longestOnes(nums, k)
print(res)