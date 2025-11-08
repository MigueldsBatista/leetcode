def longestOnes(self, nums, max_flips):
    left = 0
    for right in range(len(nums)):
        max_flips -= 1 - nums[right]  # Decrease flips when we encounter 0
        if max_flips < 0:
            max_flips += 1 - nums[left]  # Regain a flip when removing a 0 from window
            left += 1
    return right - left + 1