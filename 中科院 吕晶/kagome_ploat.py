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
Z=map(Kagome_eigvalues,XY)
##取第零列
ZZ=np.array(Z)[:,0]
##将它重新组织成meshgrid应该对应的形式
ZZZ=np.array(mma.partition(ZZ,len(kx)))


#绘制平面
ax.plot_surface(kx, ky, ZZZ, cmap=cm.coolwarm)

1+1

		
plt.show()

