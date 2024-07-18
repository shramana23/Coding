class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def rec(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return 

            if openN < n:
                stack.append('(')
                rec(openN+1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(')')
                rec(openN, closeN + 1)
                stack.pop()

        rec(0, 0)
        return res
                
        