class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = (r + l) // 2
            row = mid // n
            col = mid % n
            val = matrix[mid // n][mid % n]
            if target == val:
                return True
            else:
                if target < val:
                    r = mid - 1
                else:
                    l = mid + 1
        return False