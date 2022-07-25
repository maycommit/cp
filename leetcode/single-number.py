from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for x in nums:
            print(bin(res), bin(x))
            res ^= x

        print(res)
        return res

s = Solution()
s.singleNumber([2,2,1])
s.singleNumber([4,1,2,1,2])
s.singleNumber([1])

