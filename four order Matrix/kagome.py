from eigvalue import *
import numpy as np
def Kagome_Eigvalues(Input) :

	##修改函数
	kx=Input[0]
	ky=Input[1]
	### 以下定义矩阵元
	
	#####这是举例矩阵
	a11=a22=a33=a44=float(3/2)
	a12=0
	a13=-(1/2)*np.exp(-(kx/2)*1j)*np.cos(np.sqrt(3)*ky/2)-np.exp(kx*1j)
	a14=1j*(np.sqrt(3)/2)*np.exp(-(kx/2)*1j)*np.sin(np.sqrt(3)*ky/2)
	a21=0
	a23=a14
	a24=-(3/2)*np.exp(-(kx/2)*1j)*np.cos(np.sqrt(3)*ky/2)
	a31=a13.conjugate()
	a32=a23.conjugate()
	a34=0
	a41=a14.conjugate()
	a42=a24.conjugate()
	a43=0

	############矩阵元定义完成
	
	##### 构造H矩阵
	H = np.array([[a11, a12, a13,a14], 
	[a21, a22, a23,a24],
	[a31, a32, a33,a34],
	[a41, a42, a43,a44],
	],dtype=complex)
	
	##### 调用函数Eigvalues()获取矩阵H的特征值
	eigvalue = Eigvalues(H)
	eigvalue=eigvalue.tolist()
	return eigvalue
	##### 返回特征值



