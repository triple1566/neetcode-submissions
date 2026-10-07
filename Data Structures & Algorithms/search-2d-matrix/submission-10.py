class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # **Constraints:**
        # `m == matrix.length`
        # `n == matrix[i].length`
        # `1 <= m, n <= 100`
        # `-10000 <= matrix[i][j], target <= 10000`
        m, n = len(matrix)-1, len(matrix[0])-1
        left, right = 0, m
        row=-1
        while left <= right:
            mid = (left+right)//2
            if matrix[mid][0]<=target<=matrix[mid][n]:
                row = mid
                break
            elif target < matrix[mid][0]:
                right = mid-1
                continue
            elif matrix[mid][n] < target:
                left = mid+1
        if row==-1:
            return False
        left, right = 0, n
        while left<=right:
            mid = (left+right)//2
            if matrix[row][mid] == target:
                return True
            elif target < matrix[row][mid]:
                right = mid-1
            elif matrix[row][mid] < target:
                left = mid+1
        return False
            