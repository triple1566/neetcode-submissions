class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset_arr = [[]]
        index=0
        def dfs(subset,i):
            if i>=len(nums):
                return
            include = subset.copy()
            exclude = subset.copy()
            include.append(nums[i])
            subset_arr.append(include)
            dfs(include,i+1)
            dfs(exclude,i+1)
            return

        dfs([],index)
        return subset_arr