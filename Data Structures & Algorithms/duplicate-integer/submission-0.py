class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        p1 = 0
        length = len(nums)
        for p1 in range(length-1):
            i = p1+1
            print(i)
            while i<length:
                if (i==p1):
                    i+=1
                    continue
                elif (nums[i]==nums[p1]):
                    return True
                i+=1
        return False