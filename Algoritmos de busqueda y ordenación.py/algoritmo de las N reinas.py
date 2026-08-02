def dfs_n_queens(n):
    if n < 1:
        return []

    solutions = []

    def is_safe(board, row, col):
        for r in range(row):
            c = board[r]
            # Misma columna o misma diagonal
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def dfs(row, board):
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board.append(col)
                dfs(row + 1, board)
                board.pop()

    dfs(0, [])

    return solutions