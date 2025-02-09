# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,v1 in enumerate(nums):
            v2 = target-v1
            if v2 in d:
                return [d[v2],i]
            d[v1] = i