def min_edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)

    # 建立一個 (m+1) x (n+1) 的矩陣
    # dp[i][j] 代表 str1 前 i 個字元轉換成 str2 前 j 個字元的最少步數
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 初始化第一列與第一欄
    for i in range(m + 1):
        dp[i][0] = i  # str1 轉成空字串，需要全部刪除
    for j in range(n + 1):
        dp[0][j] = j  # 空字串轉成 str2，需要全部插入

    # 填充矩陣
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                # 如果字元相同，不需要額外操作
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # 如果字元不同，取 插入、刪除、替換 三者中的最小值 + 1
                dp[i][j] = 1 + min(
                    dp[i][j - 1],    # 插入 (Insert)
                    dp[i - 1][j],    # 刪除 (Delete)
                    dp[i - 1][j - 1] # 替換 (Replace)
                )

    return dp[m][n]

# 測試
word1 = "kitten"
word2 = "sitting"
result = min_edit_distance(word1, word2)
print(f"'{word1}' 轉為 '{word2}' 的最小編輯距離是: {result}")