class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        def modify(i, j):
            if i<0 or i>=m or j<0 or j>=n or board[i][j] != 'O':
                return 
            board[i][j] = 'D'
            modify(i+1, j)
            modify(i, j+1)
            modify(i-1, j)
            modify(i, j-1)

        for i in [0, m-1]:
            for j in range(n):
                if board[i][j] == 'O':
                    modify(i, j)
        for j in [0, n-1]:
            for i in range(m):
                if board[i][j] == 'O':
                    modify(i, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'D':
                    board[i][j] = 'O'
        
                


        