class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows - 1
        while left <= right:
            row = (left + right)//2
            if target > matrix[row][-1]:
                left = row + 1
            elif target < matrix[row][0]:
                right = row - 1
            else:
                break
        if not (left <= right):
            return False

        row = (left + right)//2
        left, right = 0, cols - 1
        while left <= right:
            mid = (left + right)//2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
        return False
