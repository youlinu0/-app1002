import numpy as np
import matplotlib.pyplot as plt

# 設定畫布為經典 ChatGPT 墨綠色底色
plt.figure(figsize=(7, 7), facecolor='#10a37f')
ax = plt.gca()
ax.set_facecolor('#10a37f')

# 單瓣基礎幾何參數：外端半圓弧 + 延伸直邊
theta = np.linspace(-np.pi/2, np.pi/2, 100)
r = 0.38      # 圓弧半徑
l = 0.72      # 直線段長度
d = 0.40      # 偏置距離

# 構造單瓣輪廓路徑 (直邊 -> 半圓弧 -> 直邊)
x_petal = np.concatenate([np.linspace(0, l, 60), l + r * np.sin(theta + np.pi/2), np.linspace(l, 0, 60)])
y_petal = np.concatenate([np.full(60, -r) + d,   r * np.cos(theta + np.pi/2) + d,  np.full(60, r) + d])

# 6 個花瓣繞中心每隔 60 度 (pi/3) 旋轉一次
angles = [0, np.pi/3, 2*np.pi/3, np.pi, 4*np.pi/3, 5*np.pi/3]

for phi in angles:
    # 2D 旋轉矩陣變換
    x = x_petal * np.cos(phi) - y_petal * np.sin(phi)
    y = x_petal * np.sin(phi) + y_petal * np.cos(phi)
    
    # 繪製單個白色迴旋瓣 (使用與奧運五環相同風格的 plt.plot)
    plt.plot(x, y, color='white', lw=10, solid_capstyle='round')

plt.axis('equal')
plt.axis('off')
plt.tight_layout()
plt.show()

