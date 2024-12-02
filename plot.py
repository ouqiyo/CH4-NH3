import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 读取数据文件，假设没有标题行
data = np.loadtxt('/home/xsj/lk/1126-1203/SandiaD_LTS_1/postProcessing/sample/0.25/axisSample_T_O2_p.xy')

# 使用pandas读取 'axisSample_U.xy' 文件
U_data = pd.read_csv('postProcessing/sample/0.25/axisSample_U.xy', delim_whitespace=True, header=None)

# 你可能需要将 'U' 数据添加到原始数据中，假设你要将 'U' 数据添加到 'data' 中
# 比如在这里，假设 U_data 的第四列是需要的 U 数据
U = U_data[3]

# 假设第一列是 z 值
z = data[:, 0]

# 假设其他列是参数值，根据你的实际数据格式修改
param1 = data[:, 1]
param2 = data[:, 2]
param3 = data[:, 3]
param4 = U  # 使用 U 数据作为 param4

# 创建一个 2x2 的子图，4个子图
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# 绘制每个参数在不同的子图上
axs[0, 0].plot(z, param1, label='T', color='blue')
axs[0, 0].set_xlabel('z')
axs[0, 0].set_ylabel('T')
axs[0, 0].grid(True)

axs[0, 1].plot(z, param2, label='O2', color='green')
axs[0, 1].set_xlabel('z')
axs[0, 1].set_ylabel('O2')
axs[0, 1].grid(True)

axs[1, 0].plot(z, param3, label='p', color='red')
axs[1, 0].set_xlabel('z')
axs[1, 0].set_ylabel('p')
axs[1, 0].grid(True)

axs[1, 1].plot(z, param4, label='U', color='orange')  # 使用 param4
axs[1, 1].set_xlabel('z')
axs[1, 1].set_ylabel('U')
axs[1, 1].grid(True)

# 调整子图布局，避免重叠
plt.tight_layout()

# 保存图像
plt.savefig('result.png')
