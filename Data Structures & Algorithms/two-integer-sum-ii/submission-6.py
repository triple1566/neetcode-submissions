class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Constraints:
        # 2 <= numbers.length <= 30000
        # -1000 <= numbers[i] <= 1000
        # -1000 <= target <= 1000

        # Requirements:
        # Your solution must use O(1) additional space.
        # There will always be exactly one valid solution.

        # Initial thoughts:
        # Since numbers is already sorted, we are free to use the binary search algorithm.
        # Since we must only use O(1) additional space, we cannot convert the list into a hashset, or use hashmaps to store the pairs.

        # Solution attempt: 
        # Iterate through numbers. For every element in numbers, 
        # find if target-element exists in numbers. 
        # For this searching part, we will use binary search.

        # Edge cases:
        # There might be multiple same elements that contribute to the solution

        # Code:
        index=[0,len(numbers)-1]
        while index[0] <= index[1]:
            if numbers[index[0]] + numbers[index[1]] == target:
                return [index[0]+1,index[1]+1]
            elif numbers[index[0]] + numbers[index[1]] > target:
                index[1]-=1
            elif numbers[index[0]] + numbers[index[1]] < target:
                index[0]+=1
        return []
            
            





  