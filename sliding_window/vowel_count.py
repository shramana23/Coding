class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        v = ['a', 'o', 'i', 'e', 'u']
        ans = 0
        start = 0
        end = 0
        i = 0
        vcount = 0

        while(i < n):
            if s[i] in v:
                vcount += 1
            end = i
            if end - start + 1 == k:
                ans = max(ans, vcount)
                if s[start] in v:
                    vcount -= 1
                start += 1

            i += 1

        return ans


        