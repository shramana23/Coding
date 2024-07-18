class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {}
        n = len(s)
        i = 0
        ans = 0
        start = 0
        end = 0

        while(i<n):
            ch = s[i]
            if ch in h:
                while s[start] != ch:
                    h.pop(s[start])
                    start += 1
                start += 1
            h[ch] = 1
            end = i
            ans = max(ans, end-start+1)
            # print(ch, ans)
            i += 1

        return ans

        



            
            
            

        