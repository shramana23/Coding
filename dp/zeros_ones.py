class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n+1) for i in range(m+1)]
        counter = []

        for s in strs:
            zs = s.count('0')
            os = s.count('1')
            counter.append([zs, os])

        for zs, os in counter:
            for i in range(m, zs-1, -1):
                for j in range(n, os-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zs][j-os] + 1)

        return dp[-1][-1]

        