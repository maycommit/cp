from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in d:
                return [d[diff], i]

            d[nums[i]] = i

        return []







s =  Solution()
s.twoSum([2,7,11,15], 9)
s.twoSum([3,2,4], 6)
s.twoSum([3,3], 6)
s.twoSum([4,0], 4)
