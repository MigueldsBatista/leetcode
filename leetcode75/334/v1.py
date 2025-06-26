"""
Atualmente

Quais as condições básicas
vamos percorrendo a lista, o primeiro numero é atribuido a A
se encontramos um maior ele vira B

se encontramos um maior que esse e já temos B, ele vira C

mas tem alguns edge cases, precisamos saber determinar a hora que um novo número vai virar A ou B

no caso do A, um novo número deve ser atribuido a A

se o número atual for menor que o nosso A atual obviamente
e o maior número começando do indice atual é menor ou igual que B
ex [20, 100, 10, 12, 5, 13]
 
"""
from notes import array

class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        a = nums[0]
        b = None
        c = None
        cached_max = None
        has_calculated = False
        
        def get_max(arr):
            nonlocal has_calculated, cached_max
            if has_calculated:
                return cached_max
            
            if cached_max is not None and cached_max in arr:
                return cached_max
            num =  max(arr) 
            has_calculated = True
            cached_max = num
            return num
        
        for i in range(1, len(nums)):
            num = nums[i]
            has_calculated = False
            if num < a and (b is None or get_max(nums[i:]) <= b):
                a = num
                b = None
                continue
            
            if (b is None or get_max(nums[i:]) <= b) or (num > a and b is None):
                b = num if num != a else None
                continue

            if b is not None and num > b:
                c = num

            if all([a != None, b != None, c != None]):
                return True
        
        return False

# arrays = [
#     [5, 4, 3, 2, 1],
#     [2,1,5,0,4,6],
#     [20,100,10,12,5,13],

#     [1,5,0,4,1,3],
    
#     [2,5,3,4,5],
#     [5,1,5,5,2,5,4],
#     [2,4,-2,-3],
#     [1,1,-2,6],
#     [1,0,-1,0,100000000]
# ]
# array = [1,0, 10, 0, 100000000]

# for i, array in enumerate(arrays):
#     print(array)
#     print(f"Result: {res}")

res = Solution().increasingTriplet(array)
print(res)