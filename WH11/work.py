import numpy as np

def cross_entropy(p, q):
    return -np.sum(p * np.log2(q + 1e-12)) # 加上微小值避免 log(0)

def verify_with_softmax_gradient():
    p = np.array([0.5, 0.25, 0.25])
    # 初始化 z (隨機值)，透過 softmax 得到初始 q
    z = np.array([0.1, 0.1, 0.1]) 
    learning_rate = 0.1
    
    for i in range(2000):
        # Forward: z -> q
        exp_z = np.exp(z)
        q = exp_z / np.sum(exp_z)
        
        # 這裡簡化梯度計算，直接觀察 q 是否趨近 p
        # 損失函數對於 z 的梯度在 softmax 下非常優雅：grad = q - p
        grad = q - p
        z -= learning_rate * grad
        
        if i % 500 == 0:
            print(f"Iter {i}: q = {q}, Loss = {cross_entropy(p, q):.6f}")

    print(f"最終結果 q: {q}")
    print(f"目標 p: {p}")

verify_with_softmax_gradient()