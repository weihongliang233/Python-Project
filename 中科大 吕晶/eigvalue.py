from scipy import linalg as la
from scipy import optimize
import numpy as np
def Eigvalues(A) :
	evals, evecs = la.eig(A)
	return evals

