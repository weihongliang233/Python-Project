from kagome import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import ForMMA as mma

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ky = np.arange(-3, 3, 1)
kx = np.arange(-3, 3, 1)
# 构造kxky网格平面
kx,ky=np.meshgrid(kx,ky)

##压平kx和ky。
kkx=kx.flatten()
kky=ky.flatten()
XY=mma.partition(mma.riffle(kkx,kky),2)
##获取本征值
Z=map(Kagome_Eigvalues,XY)

##取第零列
ZZ=np.array(Z)[:,0]
##将它重新组织成meshgrid应该对应的形式
ZZZ=np.array(mma.partition(ZZ,len(kx)))

ZZZ.real


fig = plt.figure()
ax = fig.gca(projection='3d')

# Plot the surface.
surf = ax.plot_surface(kx, ky, ZZZ.real, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
