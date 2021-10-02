import cvxpy as cp
import numpy as np
import sys
import os
import json

pos=5
mat=3
arrow=4
states=2
health=5
actions=10




B=[]
R=[]

S=[]
T=[]

def getrow(a,b,c,d,e):
	return a*mat*arrow*states*health+b*arrow*states*health+c*states*health+d*health+e


A=np.zeros((600,0))
columns=0

def calculate(a,b,c,d,e):
	global columns
	global A
	if(e==0):
		C=np.zeros((600,1))
		C[getrow(a,b,c,d,e)]+=1
		A=np.append(A,C,axis=1)
		R.append(0)
		S.append(getrow(a,b,c,d,e))
		T.append(0)
		return
	
	# up
	if(a==4):
		if(d==0):
			C=np.zeros((600,1))
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(1,b,c,1,e)]-=0.85*0.2
			C[getrow(2,b,c,1,e)]-=0.15*0.2
			C[getrow(1,b,c,0,e)]-=0.85*0.8
			C[getrow(2,b,c,0,e)]-=0.15*0.8
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(1)

		if(d==1):
			C=np.zeros((600,1))
			C[getrow(a,b,0,0,min(e+1,4))]-=0.5
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(1,b,c,1,e)]-=0.85*0.5
			C[getrow(2,b,c,1,e)]-=0.5*0.15
			A=np.append(A,C,axis=1)
			R.append(-40)
			S.append(getrow(a,b,c,d,e))
			T.append(1)


	if(a==3):
		if d==0:
			C=np.zeros((600,1))
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(4,b,c,1,e)]-=0.85*0.2
			C[getrow(2,b,c,1,e)]-=0.15*0.2
			C[getrow(4,b,c,0,e)]-=0.85*0.8
			C[getrow(2,b,c,0,e)]-=0.15*0.8
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(1)
		if d==1:
			C=np.zeros((600,1))
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(4,b,c,0,e)]-=0.5*0.85
			C[getrow(2,b,c,0,e)]-=0.5*0.15
			C[getrow(4,b,c,1,e)]-=0.85*0.5
			C[getrow(2,b,c,1,e)]-=0.5*0.15
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(1)

		

	# left

	if(a==4):
		if(d==0):
			C=np.zeros((600,1))
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(0,b,c,1,e)]-=0.85*0.2
			C[getrow(2,b,c,1,e)]-=0.15*0.2
			C[getrow(0,b,c,0,e)]-=0.85*0.8
			C[getrow(2,b,c,0,e)]-=0.15*0.8
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(2)

		if(d==1):
			C=np.zeros((600,1))
			C[getrow(a,b,0,0,min(e+1,4))]-=0.5
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(0,b,c,1,e)]-=0.85*0.5
			C[getrow(2,b,c,1,e)]-=0.5*0.15
			A=np.append(A,C,axis=1)
			R.append(-40)
			S.append(getrow(a,b,c,d,e))
			T.append(2)


	if(a==2):
		if d==0:
			C=np.zeros((600,1))
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(4,b,c,1,e)]-=0.2
			C[getrow(4,b,c,0,e)]-=0.8
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(2)
		if d==1:
			C=np.zeros((600,1))
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(a,b,0,0,min(e+1,4))]-=0.5
			C[getrow(4,b,c,1,e)]-=0.5
			A=np.append(A,C,axis=1)
			R.append(-40)
			S.append(getrow(a,b,c,d,e))
			T.append(2)



	# down

	if(a==4):
		if(d==0):
			C=np.zeros((600,1))
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(3,b,c,1,e)]-=0.85*0.2
			C[getrow(2,b,c,1,e)]-=0.15*0.2
			C[getrow(3,b,c,0,e)]-=0.85*0.8
			C[getrow(2,b,c,0,e)]-=0.15*0.8
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(3)

		if(d==1):
			C=np.zeros((600,1))
			C[getrow(a,b,0,0,min(e+1,4))]-=0.5
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(3,b,c,1,e)]-=0.85*0.5
			C[getrow(2,b,c,1,e)]-=0.5*0.15
			A=np.append(A,C,axis=1)
			R.append(-40)
			S.append(getrow(a,b,c,d,e))
			T.append(3)


	if(a==1):
		if d==0:
			C=np.zeros((600,1))
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(4,b,c,1,e)]-=0.85*0.2
			C[getrow(2,b,c,1,e)]-=0.15*0.2
			C[getrow(4,b,c,0,e)]-=0.85*0.8
			C[getrow(2,b,c,0,e)]-=0.15*0.8
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(3)
		if d==1:
			C=np.zeros((600,1))
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(4,b,c,0,e)]-=0.5*0.85
			C[getrow(2,b,c,0,e)]-=0.5*0.15
			C[getrow(4,b,c,1,e)]-=0.85*0.5
			C[getrow(2,b,c,1,e)]-=0.5*0.15
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(3)



	# right

	if(a==4):
		if(d==0):
			C=np.zeros((600,1))
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(2,b,c,1,e)]-=0.85*0.2
			C[getrow(2,b,c,1,e)]-=0.15*0.2
			C[getrow(2,b,c,0,e)]-=0.85*0.8
			C[getrow(2,b,c,0,e)]-=0.15*0.8
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(4)

		if(d==1):
			C=np.zeros((600,1))
			C[getrow(a,b,0,0,min(e+1,4))]-=0.5
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(2,b,c,1,e)]-=0.85*0.5
			C[getrow(2,b,c,1,e)]-=0.5*0.15
			A=np.append(A,C,axis=1)
			R.append(-40)
			S.append(getrow(a,b,c,d,e))
			T.append(4)


	if(a==0):
		if d==0:
			C=np.zeros((600,1))
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(4,b,c,1,e)]-=0.85*0.2
			C[getrow(4,b,c,1,e)]-=0.15*0.2
			C[getrow(4,b,c,0,e)]-=0.85*0.8
			C[getrow(4,b,c,0,e)]-=0.15*0.8
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(4)
		if d==1:
			C=np.zeros((600,1))
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(4,b,c,0,e)]-=0.5
			C[getrow(4,b,c,1,e)]-=0.85*0.5
			C[getrow(4,b,c,1,e)]-=0.5*0.15
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(4)


	# stay

	if(a==0):
		if(d==0):
			C=np.zeros((600,1))
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(a,b,c,1,e)]-=0.2
			C[getrow(a,b,c,0,e)]-=0.8
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(5)

		if(d==1):
			C=np.zeros((600,1))
			C[getrow(a,b,c,0,e)]-=0.5
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(a,b,c,1,e)]-=0.5
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(5)


	if(a==1):
		if d==0:
			C=np.zeros((600,1))
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(1,b,c,1,e)]-=0.85*0.2
			C[getrow(2,b,c,1,e)]-=0.15*0.2
			C[getrow(1,b,c,0,e)]-=0.85*0.8
			C[getrow(2,b,c,0,e)]-=0.15*0.8
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(5)
		if d==1:
			C=np.zeros((600,1))
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(a,b,c,0,e)]-=0.5*0.85
			C[getrow(2,b,c,0,e)]-=0.5*0.15
			C[getrow(a,b,c,1,e)]-=0.85*0.5
			C[getrow(2,b,c,1,e)]-=0.5*0.15
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(5)

	if(a==2):
		if(d==0):
			C=np.zeros((600,1))
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(2,b,c,1,e)]-=0.2
			C[getrow(2,b,c,0,e)]-=0.8
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(5)

		if(d==1):
			C=np.zeros((600,1))
			C[getrow(a,b,0,0,min(e+1,4))]-=0.5
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(a,b,c,1,e)]-=0.5
			A=np.append(A,C,axis=1)
			R.append(-40)
			S.append(getrow(a,b,c,d,e))
			T.append(5)

	if(a==3):
		if(d==0):
			C=np.zeros((600,1))
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(a,b,c,1,e)]-=0.85*0.2
			C[getrow(2,b,c,1,e)]-=0.15*0.2
			C[getrow(a,b,c,0,e)]-=0.85*0.8
			C[getrow(2,b,c,0,e)]-=0.15*0.8
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(5)

		if(d==1):
			C=np.zeros((600,1))
			C[getrow(a,b,c,0,e)]-=0.5*0.85
			C[getrow(2,b,c,0,e)]-=0.5*0.15
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(a,b,c,1,e)]-=0.85*0.5
			C[getrow(2,b,c,1,e)]-=0.5*0.15
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(5)

	if(a==4):
		if(d==0):
			C=np.zeros((600,1))
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(a,b,c,1,e)]-=0.85*0.2
			C[getrow(2,b,c,1,e)]-=0.15*0.2
			C[getrow(a,b,c,0,e)]-=0.85*0.8
			C[getrow(2,b,c,0,e)]-=0.15*0.8
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(5)

		if(d==1):
			C=np.zeros((600,1))
			C[getrow(a,b,0,0,min(e+1,4))]-=0.5
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(a,b,c,1,e)]-=0.85*0.5
			C[getrow(2,b,c,1,e)]-=0.5*0.15
			A=np.append(A,C,axis=1)
			R.append(-40)
			S.append(getrow(a,b,c,d,e))
			T.append(5)




	# shoot

	if(a==0):
		if(d==0 and c>0):
			C=np.zeros((600,1))
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(a,b,c-1,1,e-1)]-=0.25*0.2
			C[getrow(a,b,c-1,1,e)]-=0.75*0.2
			C[getrow(a,b,c-1,0,e-1)]-=0.25*0.8
			C[getrow(a,b,c-1,0,e)]-=0.75*0.8
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(6)

		if(d==1 and c>0):
			C=np.zeros((600,1))
			C[getrow(a,b,c-1,0,e-1)]-=0.5*0.25
			C[getrow(a,b,c-1,0,e)]-=0.5*0.75
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(a,b,c-1,1,e-1)]-=0.25*0.5
			C[getrow(a,b,c-1,1,e)]-=0.5*0.75
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(6)


	if(a==2):
		if d==0 and c>0:
			C=np.zeros((600,1))
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(a,b,c-1,1,e-1)]-=0.9*0.2
			C[getrow(a,b,c-1,1,e)]-=0.1*0.2
			C[getrow(a,b,c-1,0,e-1)]-=0.9*0.8
			C[getrow(a,b,c-1,0,e)]-=0.1*0.8
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(6)
		if d==1 and c>0:
			C=np.zeros((600,1))
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(a,b,0,0,min(e+1,4))]-=0.5
			C[getrow(a,b,c-1,1,e-1)]-=0.9*0.5
			C[getrow(a,b,c-1,1,e)]-=0.1*0.5
			A=np.append(A,C,axis=1)
			R.append(-40)
			S.append(getrow(a,b,c,d,e))
			T.append(6)

	if(a==4):
		if d==0 and c>0:
			C=np.zeros((600,1))
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(a,b,c-1,1,e-1)]-=0.5*0.2
			C[getrow(a,b,c-1,1,e)]-=0.5*0.2
			C[getrow(a,b,c-1,0,e-1)]-=0.5*0.8
			C[getrow(a,b,c-1,0,e)]-=0.5*0.8
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(6)
		if d==1 and c>0:
			C=np.zeros((600,1))
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(a,b,0,0,min(e+1,4))]-=0.5
			C[getrow(a,b,c-1,1,e-1)]-=0.5*0.5
			C[getrow(a,b,c-1,1,e)]-=0.5*0.5
			A=np.append(A,C,axis=1)
			R.append(-40)
			S.append(getrow(a,b,c,d,e))
			T.append(6)




	# hit

	if(a==4):
		if(d==0):
			C=np.zeros((600,1))
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(a,b,c,1,max(e-2,0))]-=0.1*0.2
			C[getrow(a,b,c,1,e)]-=0.9*0.2
			C[getrow(a,b,c,0,max(e-2,0))]-=0.1*0.8
			C[getrow(a,b,c,0,e)]-=0.9*0.8
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(7)

		if(d==1):
			C=np.zeros((600,1))
			C[getrow(a,b,0,0,min(e+1,4))]-=0.5
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(a,b,c,1,max(e-2,0))]-=0.1*0.5
			C[getrow(a,b,c,1,e)]-=0.5*0.9
			A=np.append(A,C,axis=1)
			R.append(-40)
			S.append(getrow(a,b,c,d,e))
			T.append(7)


	if(a==2):
		if(d==0):
			C=np.zeros((600,1))
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(a,b,c,1,max(e-2,0))]-=0.2*0.2
			C[getrow(a,b,c,1,e)]-=0.8*0.2
			C[getrow(a,b,c,0,max(e-2,0))]-=0.2*0.8
			C[getrow(a,b,c,0,e)]-=0.8*0.8
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(7)

		if(d==1):
			C=np.zeros((600,1))
			C[getrow(a,b,0,0,min(e+1,4))]-=0.5
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(a,b,c,1,max(e-2,0))]-=0.2*0.5
			C[getrow(a,b,c,1,e)]-=0.5*0.8
			A=np.append(A,C,axis=1)
			R.append(-40)
			S.append(getrow(a,b,c,d,e))
			T.append(7)
		




	# craft

	if(a==1):
		if(d==0 and b>0):
			C=np.zeros((600,1))
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(a,b-1,min(c+1,3),1,e)]-=0.5*0.2
			C[getrow(a,b-1,min(c+2,3),1,e)]-=0.35*0.2
			C[getrow(a,b-1,min(c+3,3),1,e)]-=0.15*0.2
			C[getrow(a,b-1,min(c+1,3),0,e)]-=0.5*0.8
			C[getrow(a,b-1,min(c+2,3),0,e)]-=0.35*0.8
			C[getrow(a,b-1,min(c+3,3),0,e)]-=0.15*0.8
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(8)

		if(d==1 and b>0):
			C=np.zeros((600,1))
			C[getrow(a,b-1,min(c+1,3),0,e)]-=0.5*0.5
			C[getrow(a,b-1,min(c+2,3),0,e)]-=0.35*0.5
			C[getrow(a,b-1,min(c+3,3),0,e)]-=0.15*0.5
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(a,b-1,min(c+1,3),1,e)]-=0.5*0.5
			C[getrow(a,b-1,min(c+2,3),1,e)]-=0.35*0.5
			C[getrow(a,b-1,min(c+3,3),1,e)]-=0.15*0.5
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(8)



	# gather

	if(a==3 and b<=2):
		if(d==0):
			C=np.zeros((600,1))
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(a,min(b+1,2),c,1,e)]-=0.75*0.2
			C[getrow(a,b,c,1,e)]-=0.25*0.2
			C[getrow(a,min(b+1,2),c,0,e)]-=0.75*0.8
			C[getrow(a,b,c,0,e)]-=0.25*0.8
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(9)

		if(d==1):
			C=np.zeros((600,1))
			C[getrow(a,min(b+1,2),c,0,e)]-=0.5*0.75
			C[getrow(a,b,c,0,e)]-=0.5*0.25
			C[getrow(a,b,c,d,e)]+=1
			C[getrow(a,min(b+1,2),c,1,e)]-=0.75*0.5
			C[getrow(a,b,c,1,e)]-=0.5*0.25
			A=np.append(A,C,axis=1)
			R.append(-20)
			S.append(getrow(a,b,c,d,e))
			T.append(9)

	


	



	# none





for i in range(pos):
	for j in range(mat):
		for k in range(arrow):
			for l in range(states):
				for m in range(health):
					calculate(i,j,k,l,m)

original_stdout = sys.stdout # Save a reference to the original standard output

Rew=np.array(R)
x = cp.Variable(shape=(1936,1), name="x")
alpha=np.zeros((600,1))
alpha[getrow(4,2,3,1,4)]+=1
alpha2=np.zeros(600)
alpha2[getrow(4,2,3,1,4)]+=1
constraints = [cp.matmul(A, x) == alpha, x>=0]
objective = cp.Maximize(cp.matmul(Rew,x))
problem = cp.Problem(objective, constraints)

solution = problem.solve()
xy=list(x)
i=0
j=0
Act=np.zeros(600)
for i in range(600):
	num=0
	while (j<len(S)and S[j]==i):
		if(num<=x.value[j]):
			Act[i]=T[j]
			num=max(num,x.value[j])

		j+=1



def name_of_action(i):
    if i==1:
        return "UP"
    elif i==2:
        return "LEFT"
    elif i==4:
        return "RIGHT"
    elif i==3:
        return "DOWN"
    elif i==5:
        return "STAY"
    elif i==6:
        return "SHOOT"
    elif i==7:
        return "HIT"
    elif i==9:
        return "GATHER"
    elif i==8:
        return "CRAFT"
    else:
        return "NONE"




l2=[]
for i in range(pos):
	for j in range(mat):
		for k in range(arrow):
			for l in range(states):
				for m in range(health):
					l1=[]
					l3=[]
					if(i==0):
						l1.append('W')
					elif(i==1):
						l1.append('N')
					elif(i==2):
						l1.append('E')
					elif i==3:
						l1.append('S')
					elif i==4:
						l1.append('C')

					if j==0:
						l1.append(0)
					elif j==1:
						l1.append(1)
					elif j==2:
						l1.append(2)

					if k==0:
						l1.append(0)
					elif k==1:
						l1.append(1)
					elif k==2:
						l1.append(2)
					elif k==3:
						l1.append(3)

					if l==0:
						l1.append('D')
					elif l==1:
						l1.append('R')

					if m==0:
						l1.append(0)
					elif m==1:
						l1.append(25)
					elif m==2:
						l1.append(50)
					elif m==3:
						l1.append(75)
					elif m==4:
						l1.append(100)

					l3.append(l1)
					l3.append(name_of_action(Act[getrow(i,j,k,l,m)]))
					l2.append(l3)
					

thisdict={
	
}
thisdict["a"]=A.tolist()
thisdict["r"]=R
thisdict["alpha"]=alpha2.tolist()

x2=[]
for i in range(1936):
	x2.append(x.value[i][0])
thisdict["x"]=x2
thisdict["policy"]=l2
thisdict["objective"]=solution



original = sys.stdout
os.mkdir("./outputs")

with open('./outputs/part_3_output.json','w') as outfile:
	json.dump(thisdict,outfile)





