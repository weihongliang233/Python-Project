from kagome import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ky = np.arange(-3, 3, 0.25)
kx = np.arange(-3, 3, 0.25)
# 构造kxky网格平面
kx,ky=np.meshgrid(kx,ky)
## 调用函数Kagome_eigvalues()获取特征值
z=Kagome_eigvalues(kx,ky)
#绘制平面
ax.plot_surface(kx, ky, z, cmap=cm.coolwarm)

		
plt.show()
