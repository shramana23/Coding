class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = 0
        res = ""
        for i in range(len(s)):
            mid = s[i]
            j = i
            count = 1
            while True:
                if j-count < 0:
                    break
                if j+count == len(s):
                    break
                if s[j-count] == s[j+count]:
                    count += 1
                    continue
                else:
                    break
            # print(mid)
            # print(count)
            # print(j)
            if (count * 2) - 1 > ans:
                res = s[j-count+1: j+count]
                # print(f"res --- {res}")
                ans = (count * 2) - 1

        for i in range(1, len(s)):
            mid = s[i]
            l = i - 1
            r = i
            if s[l] != s[r]:
                continue
            count = 1
            while True:
                if l-count < 0:
                    break
                if r+count == len(s):
                    break
                if s[l-count] == s[r+count]:
                    count += 1
                    continue
                else:
                    break
            # print(mid)
            # print(count)
            # print(j)
            if (count * 2) > ans:
                res = s[l-count+1: r+count]
                # print(f"res --- {res}")
                ans = (count * 2) - 1
        return res

            
                

        