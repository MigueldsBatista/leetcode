"""

11. Container With Most Water
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

oq eu pensei, nós precisamos de uma linha na esquerda e outra na direita
precisamos de uma variável eixo x tal que vai aumentando conforme o loop

basicamente precisamos encontrar a maior linha na esquerda e a maior linha na direita
separadas pelo maior eixo x possível

como identificar quais linhas escolher?

posso fazer um ponteiro esquerda e direita, mas qual o problema que eu encontrei,
eu nao posso simplismente avançar a cada iteração, nao tenho como prever quais vão ser as duas alturas certas
ex se eu for avançando 1 do ponteiro A e diminuindo 1 do ponteiro B, pode ser a combinação fosse
a primeira altura usada e a penuitima, algo do tipo

a área geralmente vai ser o minimo entre esquerda e direita vezes o eixo X

NOTE: lembrar do outro problema
 
TODO X
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Step 1: Initialize maximum area and two pointers
        maxArea = 0
        left = 0                    # Left pointer starts at beginning
        right = len(height) - 1     # Right pointer starts at end
        
        # Step 2: Continue until pointers meet
        while right > left:
            
            # Step 3: Calculate area with current pair of lines
            # Area = min_height * width
            area = min(height[left], height[right]) *  abs(right - left)

            # Step 4: Move pointer with shorter line inward
            # This gives us the best chance to find a larger area
            if height[left] > height[right]:
                right -= 1  # Right line is shorter, move right pointer left
            else:
                left += 1   # Left line is shorter or equal, move left pointer right

            # Step 5: Update maximum area found so far
            maxArea = max(maxArea, area)

        return maxArea
list = [1,8,6,2,5,4,8,3,7]
# list = [1,1]

print(Solution().maxArea(list))

"""
LeetCode 11: Container With Most Water - Two Pointer Approach

ALGORITHM EXPLANATION:
This problem asks to find two lines that can hold the maximum amount of water.
The area is calculated as: min(height[left], height[right]) * (right - left)

KEY INSIGHT:
Use two pointers starting from both ends. The water level is limited by the shorter line,
so we should move the pointer of the shorter line inward, hoping to find a taller line.

STEP-BY-STEP ALGORITHM:
1. Initialize two pointers: left = 0, right = n-1
2. Calculate area with current pair of lines
3. Move the pointer with the shorter line inward
   - If height[left] < height[right]: move left++
   - If height[right] <= height[left]: move right--
4. Keep track of maximum area seen so far
5. Continue until pointers meet

WHY THIS WORKS:
- Moving the pointer with the taller line would only decrease the width while 
  keeping the same height limitation (the shorter line)
- Moving the pointer with the shorter line gives us a chance to find a taller line
- This ensures we don't miss the optimal solution

TIME COMPLEXITY: O(n) - single pass with two pointers
SPACE COMPLEXITY: O(1) - only using constant extra space

EXAMPLE WALKTHROUGH:
height = [1,8,6,2,5,4,8,3,7]

Step 1: left=0, right=8, height[0]=1, height[8]=7
- area = min(1,7) * (8-0) = 1 * 8 = 8
- Since height[0] < height[8], move left++

Step 2: left=1, right=8, height[1]=8, height[8]=7  
- area = min(8,7) * (8-1) = 7 * 7 = 49
- Since height[8] <= height[1], move right--

Step 3: left=1, right=7, height[1]=8, height[7]=3
- area = min(8,3) * (7-1) = 3 * 6 = 18
- Since height[7] < height[1], move right--

Continue until left >= right...
Maximum area found: 49
"""