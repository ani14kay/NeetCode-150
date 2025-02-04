# https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        snums = set(nums)
        if len(nums)==len(snums):
            return False
        return True