class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m*n - 1

        while l <= r:
            mid = (l + r) // 2
            row, col = divmod(mid, n)

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] > target:
                r = mid - 1

            else:
                l = mid + 1

        return False

# less memory usage


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m*n - 1

        while l <= r:
            mid = (l + r) // 2
            num = matrix[mid // n][mid % n]

            if num == target:
                return True

            elif num > target:
                r = mid - 1

            else:
                l = mid + 1

        return False
