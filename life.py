import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 1. 初始化元胞网格（100x100大小，0=死亡，1=存活）
def init_grid(rows, cols, init_density=0.2):
    # 按密度随机生成初始存活元胞
    return np.random.choice([0, 1], size=(rows, cols), p=[1-init_density, init_density])

# 2. 定义元胞更新规则（康威生命游戏核心逻辑）
def update_grid(grid):
    rows, cols = grid.shape
    # 复制网格避免更新时相互干扰
    new_grid = grid.copy()
    
    # 遍历每个元胞
    for i in range(rows):
        for j in range(cols):
            # 计算邻居总数（边缘用循环边界处理，模拟无限网格）
            neighbors = (
                grid[(i-1)%rows, (j-1)%cols] + grid[(i-1)%rows, j] + grid[(i-1)%rows, (j+1)%cols] +
                grid[i, (j-1)%cols] +                                  grid[i, (j+1)%cols] +
                grid[(i+1)%rows, (j-1)%cols] + grid[(i+1)%rows, j] + grid[(i+1)%rows, (j+1)%cols]
            )
            
            # 规则1：存活元胞邻居<2或>3 → 死亡
            if grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i, j] = 0
            # 规则2：死亡元胞邻居=3 → 复活
            elif grid[i, j] == 0 and neighbors == 3:
                new_grid[i, j] = 1
    return new_grid

# 3. 可视化动画
def animate_life(rows=100, cols=100, steps=200):
    # 初始化网格
    grid = init_grid(rows, cols)
    
    # 设置画布
    fig, ax = plt.subplots(figsize=(8, 8))
    # 用热力图展示元胞状态（黑色=死亡，白色=存活）
    im = ax.imshow(grid, cmap='binary', interpolation='nearest')
    ax.set_title('Conway\'s Game of Life (Python 模拟)')
    
    # 定义每帧更新函数
    def update(frame):
        nonlocal grid
        grid = update_grid(grid)
        im.set_data(grid)
        return [im]
    
    # 创建动画（每100ms更新一帧，共steps帧）
    anim = animation.FuncAnimation(
        fig, update, frames=steps, interval=100, blit=True
    )
    
    # 显示动画
    plt.show()

# 运行模拟（100x100网格，演化200步）
if __name__ == "__main__":
    animate_life(rows=100, cols=100, steps=200)