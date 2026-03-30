class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        right = len(matrix) -1
        mtx_len = len(matrix[0])
        while left <= right:
            mid = (left + right) // 2
            curr_min = matrix[mid][0]
            curr_max = matrix[mid][mtx_len - 1]
            if target > curr_max:
                left = mid + 1
            elif target < curr_min:
                right = mid - 1
            else:
                l = 0
                r = mtx_len - 1
                while l <= r:
                    curr_mid = (l + r) // 2
                    if matrix[mid][curr_mid]< target:
                        l = curr_mid + 1
                    elif matrix[mid][curr_mid] > target:
                        r = curr_mid - 1
                    else:
                        return True
                return False
        return False

            







