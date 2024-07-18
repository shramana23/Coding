class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(l, r, idx):
            arr = matrix[idx]
            # print(l)
            # print(r)
            # print(arr)
            # print(mid)
            # return

            while(l<=r):
                mid = (l + r) // 2
                if arr[mid] == target:
                    return True
                if arr[mid] >= target:
                    r = mid -1
                else:
                    l = mid + 1
            
            return False

        m = len(matrix)
        n = len(matrix[0])
        for r in range(m):
            if matrix[r][0] <= target <= matrix[r][n-1]:
                return binary_search(0, n-1, r) 
        
        return False
        