class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i, n in enumerate(nums):
            comp = target - n
            if comp in hmap:
                return [hmap[comp], i]
            else:
                hmap[n] = i
        return -1