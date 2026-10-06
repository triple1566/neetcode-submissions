class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        starterslist = set()
        numset = set()
        # O(N)
        for num in nums:
            numset.add(num)
        # O(N)
        for num in nums:
            if num-1 not in numset:
                starterslist.add(num)
        max_length = 1
        for seq in starterslist:
            length = 0
            i = seq
            while i in numset:
                length+=1
                i+=1
            if max_length < length:
                max_length = length
        return max_length
            