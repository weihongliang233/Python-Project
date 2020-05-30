from kagome import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from ForMMA import *


fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ky = np.arange(-4, 4, 0.5)
kx = np.arange(-4, 4, 0.5)
# 构造kxky网格平面
kx,ky=np.meshgrid(kx,ky)

##压平kx和ky。
kkx=kx.flatten()
kky=ky.flatten()
XY=mma.partition(mma.riffle(kkx,kky),2) 
##获取本征值
Z=mma.map(Kagome_Eigvalues,XY)
##取第各列
for j in range(0,4):
	ZZ=np.array(Z)[:,j]
	##将它重新组织成meshgrid应该对应的形式
	ZZZ=np.array(mma.partition(ZZ,len(kx)))
	fig=plt.figure()
	ax=Axes3D(fig)
	ax.scatter(kx.flatten().tolist(),ky.flatten().tolist(),ZZZ.flatten().tolist())
"""
ZZ=[]
for i in range(0,len(np.array(Z)[0])) :
	ZZ.append(np.array(Z)[:,i])
##将它重新组织成meshgrid应该对应的形式
ZZZ=[]
for i in range(0,len(ZZ)) :
	ZZZ.append(np.array(mma.partition(ZZ[i],len(kx))))

ZZ
"""


# Plot the surface.
for i in range(0,len(ZZZ)) :
	surf = ax.plot_surface(kx, ky, ZZZ[i].real,linewidth=0, antialiased=False)
                                                                                           
# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
