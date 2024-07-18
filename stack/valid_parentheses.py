class Solution:
    def isValid(self, s: str) -> bool:
        stack = [s[0]]
        # o = ['(', '{', '[']
        c = {']': '[', ')':'(', '}': '{'}
        for st in s[1:]:
            if st in c:
                if not stack or stack[-1] != c[st]:
                    return False
                stack.pop()
                continue
            stack.append(st)
        
        return len(stack) == 0
            

        