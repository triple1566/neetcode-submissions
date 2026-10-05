class Solution:
    #2 <= nums.length <= 100,000
    #-30 <= nums[i] <= 30
    #The product of any prefix or suffix of nums
    #is guaranteed to fit in a 32-bit integer.
    #base 10:(2^31)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initial thought: brute force:
        # for every i in nums, loop through all non-i elements, and append it to the result array.
        # Consequences: n^2 time complexity.
        # Solution?
        res_list = []
        if nums.count(0)>1:
            for num in nums:
                res_list.append(0)
            return res_list
        total_mult = 1
        zero_exist = False
        # O(N)
        for num in nums:
            if num == 0:
                zero_exist = True
                continue
            total_mult = total_mult * num
        # O(N)
        for i in range(len(nums)):
            if zero_exist and nums[i]!=0:
                res_list.append(0)
            elif zero_exist and nums[i]==0:
                res_list.append(total_mult)
            else:
                res_list.append(int(total_mult/nums[i]))
        return res_list
        