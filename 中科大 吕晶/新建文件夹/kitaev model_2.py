import numpy as np
import matplotlib.pyplot as plt
import gauss_integral

E0=0
gama=0.1
Kb=8.61735e-02
eV=4
T=0.1
#Em=0.6
try:
	def Crrent(KD,Em) :
		def F(E) :
			def fermi_distrubution(energy,temperature) : # 定义费米分布
			
				f=1/(np.exp(-energy/(Kb*temperature))+1)
				return f	
			# 以下计算小格林函数
			gr1=(1/4)*((np.sqrt(3)/(3*np.pi*(0.5*KD)**2))*(Em-(E+E0))*np.log(abs(1+Em/(E+E0)))+1/(E+E0+0.5*KD))+1j*(1/4)*np.pi*(np.sqrt(3)/(3*np.pi*(0.5*KD)**2))*(E+E0)
			gr2=(1/2)*(1/(E-E0-0.5*KD+1j*0.000001))
			# 计算大格林函数
			GR1=gr1/(1+1j*gr1*gama)
			GR2=gr2/(1+1j*gr2*gama)
			# 计算被积函数，被积函数本应是电流V,温度T,态密度和跃迁矩阵元(耦合成gama参数)的函数，但是这里只考虑I-V的关系
			Ff=(gama**2/2*np.pi)*(GR1*GR1.conjugate()+GR2*GR2.conjugate())*(fermi_distrubution(E+eV,T)-fermi_distrubution(E,T))
			return Ff
		# 以下计算高斯积分
		I=gauss_integral.Gauss_integral(-6,6,F) 
		return I
except  RuntimeWarning:
	pass
# 电压变化，画出I-V曲线图

'''I=[]
for KD in KD:
	Em=3*KD
	I.append(Crrent(KD))'''
KD=np.arange(0,20,0.1)
fig, ax = plt.subplots()
ax.plot(KD, [Crrent(float(KD[1]),float(KD[k])) for k in range(0,KD.size)],label='$E0=0,Em=3KD,Gama=0.1,eV=4,T=0.1$')
ax.set(xlabel='KD', ylabel='Crrent')
ax.grid()
legend = ax.legend(loc = 'upper center', frameon=False, shadow=False, fontsize=10)
plt.show()
