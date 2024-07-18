class Solution:
    def validPalindrome(self, s: str) -> bool:
        r = len(s) - 1
        l = 0

        while(l<=r):
            if s[l] != s[r]:
                without_left = s[l:r]
                without_right = s[l+1:r+1]
                return without_left == without_left[::-1] or without_right == without_right[::-1]
            l += 1
            r -= 1

        return True
        