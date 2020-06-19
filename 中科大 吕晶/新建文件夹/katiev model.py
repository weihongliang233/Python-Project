import numpy as np
import matplotlib.pyplot as plt
import gauss_integral
E0=0
D=0.2
Kb=8.61735e-02 #单位是eV/K
gama=0.1
T=0
fig, ax = plt.subplots()
for K in range(1,2):
	KD=K*D
	Em=3*KD
	def Crrent(eV) :
		def F(E) :
			def fermi_distrubution(energy,temperature) : # 定义费米分布
				if temperature == 0 :
					if energy <= 0 :
						f=1
					else:
						f=0
				else :
					f=1/(np.exp(energy/(Kb*temperature))+1)
				return f	
				# 以下计算小格林函数
			gr1=(1/4)*((np.sqrt(3)/(3*np.pi*(0.5*KD)**2))*(Em-(E+E0)*np.log(abs(1+Em/(E+E0))))+1/(E+E0+0.5*KD))+1j*(1/4)*np.pi*(np.sqrt(3)/(3*np.pi*(0.5*KD)**2))*(E+E0)
			gr2=(1/2)*(1/(E-E0-0.5*KD+1j*0.000001))
			# 计算大格林函数

			print(gr1)
			

			GR1=gr1/(1+1j*gr1*gama)
			GR2=gr2/(1+1j*gr2*gama)
			# 计算被积函数，被积函数本应是电流V,温度T,态密度和跃迁矩阵元(耦合成gama参数)的函数，但是这里只考虑I-V的关系
			F=(gama**2/(2*np.pi))*(GR1*GR1.conjugate()+GR2*GR2.conjugate())*(fermi_distrubution(E+eV,T)-fermi_distrubution(E,T))
			return F
			# 以下计算积分
		I=abs(gauss_integral.Gauss_integral(-6,6,F)) #高斯积分函数积分
		return I
	eV=np.arange(0,10,0.01)
	I=[]
	for x in eV:
		I.append(Crrent(x))
	ax.plot(eV, I,label='$E0=0,Em=3KD,D=0.2,Gama=0.1$'+'K='+str(K))
# 电压变化，画出I-V曲线图

	'''if Crrent(x) > 0:
		fffff.append(x)
print('eV must greater than ' + str(fffff[0])+' can exsit Crrent!')'''
#ax.fill_between(V,I,color='green',alpha=0.5) #渲染底部颜色
ax.set(xlabel='eV', ylabel='Crrent')
legend = ax.legend(loc = 'upper center', frameon=False, shadow=False, fontsize=10)
ax.grid()
plt.show()
