class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        # Binary search to find candidate row
        up = 0
        down = len(matrix) - 1
        row = -1

        while up <= down:
            mid = (up + down) // 2
            if matrix[mid][0] <= target:
                row = mid
                up = mid + 1
            else:
                down = mid - 1

        if row == -1:
            return False

        # If target is outside the row range, exit early
        if target > matrix[row][-1]:
            return False

        # Binary search within the row
        left = 0
        right = len(matrix[row]) - 1

        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] < target:
                left = mid + 1
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                return True

        return False
