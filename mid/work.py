import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import random

# --- 模擬數據引擎 ---
class FakeStockEngine:
    @staticmethod
    def get_data(days=100):
        # 產生一個正弦波 + 隨機雜訊，模擬股價波動
        t = np.linspace(0, 4 * np.pi, days)
        noise = np.random.normal(0, 0.1, days)
        prices = np.sin(t) + 1.5 + noise # 確保價格為正數
        # 正規化到 0~1
        return (prices - prices.min()) / (prices.max() - prices.min())

# --- 基礎 3D 結構 ---
class Maze3DGenerator:
    def __init__(self, width, height, depth):
        self.width, self.height, self.depth = width, height, depth
        self.maze = [[[1 for _ in range(width)] for _ in range(height)] for _ in range(depth)]

# --- 整合後的預測優化器 ---
class StockOptimizationMaze(Maze3DGenerator):
    def __init__(self, width, height, depth, data):
        super().__init__(width, height, depth)
        self.data = data
        self.loss_map = np.zeros((depth, height, width))

    def gradient_loss(self, w1, w2):
        """ 模擬梯度引擎：計算給定權重下的預測誤差 """
        error = 0
        for i in range(2, len(self.data)):
            # 簡單模型：今天預測 = w1 * 昨天 + w2 * 前天
            pred = w1 * self.data[i-1] + w2 * self.data[i-2]
            error += (pred - self.data[i])**2
        return error / len(self.data)

    def generate_and_prune(self, threshold=0.05):
        """ 第九點：根據 Loss 進行權重修剪 """
        print(f"正在分析模擬數據，執行權重修剪 (門檻: {threshold})...")
        for z in range(self.depth):
            for y in range(self.height):
                for x in range(self.width):
                    # 將座標轉為權重範圍 0.0 ~ 2.0
                    w1, w2 = (x / self.width) * 2, (y / self.height) * 2
                    loss = self.gradient_loss(w1, w2)
                    self.loss_map[z][y][x] = loss
                    # 若誤差太高，設為牆壁(1)；誤差低，設為路徑(0)
                    self.maze[z][y][x] = 0 if loss < threshold else 1
        
        # 標記起點與終點
        self.maze[0][1][1] = 'IN'
        self.maze[self.depth-1][self.height-2][self.width-2] = 'OUT'

    def hill_climbing(self):
        """ 爬山法：在白色區域尋找局部最優參數 """
        curr = (0, 1, 1)
        for _ in range(100):
            z, y, x = curr
            self.maze[z][y][x] = 'P' # 標記路徑
            neighbors = [(z, y+dy, x+dx) for dy, dx in [(0,1),(0,-1),(1,0),(-1,0)]]
            
            best_n = curr
            min_l = self.loss_map[z][y][x]
            for nz, ny, nx in neighbors:
                if 0 <= ny < self.height and 0 <= nx < self.width:
                    if self.maze[nz][ny][nx] != 1 and self.loss_map[nz][ny][nx] < min_l:
                        min_l = self.loss_map[nz][ny][nx]
                        best_n = (nz, ny, nx)
            if best_n == curr: break
            curr = best_n

    def draw(self):
        fig, axes = plt.subplots(1, self.depth, figsize=(15, 5))
        cmap = mcolors.ListedColormap(['white', 'black', 'blue', 'lime']) # 0:路, 1:牆, 藍:進出, 綠:路徑
        for z in range(self.depth):
            img = np.zeros((self.height, self.width))
            for y in range(self.height):
                for x in range(self.width):
                    val = self.maze[z][y][x]
                    if val == 1: img[y][x] = 1
                    elif val == 'IN' or val == 'OUT': img[y][x] = 2
                    elif val == 'P': img[y][x] = 3
            axes[z].imshow(img, cmap=cmap)
            axes[z].set_title(f"Layer {z}")
        plt.show()

# --- 執行 ---
data = FakeStockEngine.get_data()
opt = StockOptimizationMaze(21, 21, 3, data)
opt.generate_and_prune(threshold=0.03) # 調整此數值看修剪效果
opt.hill_climbing()
opt.draw()