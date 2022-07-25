from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i, j = 0, 0
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

            j += 1

        print(nums)


s = Solution()
s.moveZeroes([0,1,0,3,12])
s.moveZeroes([0,0,1])
