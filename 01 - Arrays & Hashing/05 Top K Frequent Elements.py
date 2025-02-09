# https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        s=set(nums)
        for i in s:
            d[i] = nums.count(i)
        dl = sorted(d.items(), key=lambda item : item[1], reverse=True)
        return list(dl[i][0] for i in range(k))
    
 # Self Note : Try a Better Approach!