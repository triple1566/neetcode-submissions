class Solution:
    # 0 <= nums.length <= 100,000
    # -10^9 <= nums[i] <= 10^9

    def recursiveNextNum(self,num_set,number,seq_length):
        # i in set -> O(1)
        if number in num_set:
            res = self.recursiveNextNum(num_set,number+1,seq_length+1)
            return res
        else:
            return seq_length


    def longestConsecutive(self, nums: List[int]) -> int:
        # Edge cases:
        # when there are no elements.
        if len(nums)==0:
            return 0
        # when there is only one element...
        if len(nums)==1:
            return 1

        # Requirement:
        # Must run in O(N) time.

        #Thought: should I sort the array first?
        # No. Sorting gives O(NLogN) at best. this is greater than O(N)

        # set conversion --> O(1)
        num_set = set(num for num in nums)

        # Set longest sequence number
        longest = 1

        for num in num_set:
            length = self.recursiveNextNum(num_set, num, 0)
            if length > longest:
                longest = length
        return longest