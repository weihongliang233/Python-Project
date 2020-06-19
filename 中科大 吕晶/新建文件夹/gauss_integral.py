T = [-0.9061798459, -0.5384693101, 0.0, 0.5384693101, 0.9061798459]
C= [0.2369268851, 0.4786286705, 0.5688888889, 0.4786286705, 0.2369268851]

def Gauss_integral(a,b,f):
	g=0
	for i in range(len(T)):
		try:
			x=((b-a)*T[i]+b+a)/2.0
			g=g+C[i]*f(x)
			g=((b-a)/2)*g
		except ZeroDivisionError :
			pass
	return g

