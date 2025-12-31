def solve_n_queens(n):
    res = []
    # board[i] = j 表示第 i 行的皇后放在第 j 欄
    board = [-1] * n

    def is_safe(row, col):
        for i in range(row):
            # 檢查同列或同對角線
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True

    def dfs(row):
        if row == n:
            # 找到一個解，格式化輸出
            res.append(list(board))
            return

        for col in range(n):
            if is_safe(row, col):
                board[row] = col  # 放置皇后
                dfs(row + 1)      # 往下一層搜尋
                board[row] = -1   # 回溯（清空目前位置，嘗試下一個 col）

    dfs(0)
    return res

# 執行並印出第一組解
solutions = solve_n_queens(8)
print(f"總共有 {len(solutions)} 組解。")
print("其中一組解為：", solutions[0])