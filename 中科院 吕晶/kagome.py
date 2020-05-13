from eigvalue import *
import numpy as np
def Kagome_eigvalues(Input) :

	##修改函数
	kx=Input[0]
	ky=Input[1]
	### 以下定义矩阵元
	a11=float(5/2)
	a22=1
	a33=0
	a12=-np.sqrt(3)/2
	a13=-2*np.cos(kx)
	a15=-1*float(1/2)*np.cos(kx/2-np.sqrt(3)*ky/2)
	a16=(np.sqrt(3)/2)*np.cos(kx/2-np.sqrt(3)*ky/2)
	a25=a16
	a26=3*a15
	a34=-a12
	a35=-1*float(1/2)*np.cos(kx/2+np.sqrt(3)*ky/2)
	a36=-(np.sqrt(3)/2)*np.cos(kx/2+np.sqrt(3)*ky/2)
	a45=a36
	a46=3*a35
	############矩阵元定义完成
	
	##### 构造H矩阵
	H = np.array([[a11, a12, a13,0,a15,a16], 
	[a12, a11, 0,0,a25,a26],
	[a13, 0, a11,a34,a35,a36],
	[0, 0, a34,a11,a45,a46],
	[a15, a25, a35,a45,a22,0],
	[a16, a26, a36,a46,0,a33]], dtype=float
	)
	
	##### 调用函数Eigvalues()获取矩阵H的特征值
	eigvalue = Eigvalues(H)
	eigvalue=eigvalue.tolist()
	return eigvalue
	##### 返回特征值

