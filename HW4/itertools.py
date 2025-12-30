import itertools

def generate_truth_table_inputs(n):
    # 定義可能的邏輯值
    values = [True, False]
    
    # 使用 product 進行笛卡兒積運算
    # repeat=n 表示將 values 自乘 n 次
    table = itertools.product(values, repeat=n)
    
    # 印出結果標題
    headers = [f"P{i+1}" for i in range(n)]
    print(" | ".join(headers))
    print("-" * (n * 7))
    
    # 疊代並印出每一列
    for row in table:
        print(" | ".join(str(v).ljust(5) for v in row))

# 舉例：產生 3 個變數的真值表輸入
generate_truth_table_inputs(3)