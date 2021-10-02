from client import *
import numpy as np
from numpy import random
import sys

overfit=[]
with open('overfit.txt', 'r') as read_file:
	overfit=json.load(read_file )
# answer2=[]
id='PY7YV38olDDNHyswriYZnN7yj2aULneTxJ9yTMWm03mdHMQOHk'
# answer2=get_errors(id,overfit)
# print(answer2)


def fitness(gen):
	fitness_values=np.zeros((gen.shape[0],3))
	for i in range(gen.shape[0]):
		fitness_values[i,2]=i
		fitness_values[i,0:2]=get_errors(id,list(gen[i,:]))
	arr1=fitness_values[0:pop_size,1:2]
	arr2=fitness_values[0:pop_size,0:1]
	arr3=np.add(arr1,arr2)
	fitness_values[0:pop_size,1:2]=arr3
	return fitness_values

generations=25
maxi=1e18
indi=0
to_be=[]
to_be2=np.zeros((1,12))
final=[]
def selection(gen,fitness_value,gens):
	global maxi
	global to_be2
	global to_be
	global final
	for i in range(gen.shape[0]):
		fitness_value[i,2]=i

	fitness_value=fitness_value[fitness_value[:,1].argsort()]
	

	if maxi > fitness_value[0][1]:
		to_be=list(gen[(int)(fitness_value[0][2])])
		maxi=fitness_value[0][1]
		to_be3=[]
		to_be3.extend(to_be)
		# print(to_be3)
		to_be3.append(fitness_value[0][1])
		# print(to_be3)
		final.append(to_be3)
		# print(final)

	if (gens==generations-1):
		# print(fitness_value[0][2])
		# print(to_be)
		submit(id,list(to_be))
	indices=[]
	weights=[]
	more_indices=[]
	sumi=np.sum(fitness_value, axis = 0)
	x=sumi[1]
	for i in range(int((gen.shape[0]*2)/4)):
		indices.append((int)(fitness_value[i][2]))
		weights.append(fitness_value[i][1]/x)
	weights = weights[::-1] 
	f=0
	while f==0:
		more_indices=np.random.choice(indices, gen.shape[0], weights)
		f=1
		i=0
		m=0
		while i<gen.shape[0]:
			if more_indices[i+1]==more_indices[i]:
				m=1
			i+=2
		if m==1:
			f=0
			
	after_fitness=gen[more_indices]
	return after_fitness

def crossover(after_fitness):
	i=0
	children = np.zeros((after_fitness.shape[0], 11))

	
	while i < after_fitness.shape[0]:
		f=0
		while f==0:
			position=random.randint(1,10)
			first1 = random.randint(0,pop_size-1)
			second2 = random.randint(0,pop_size-1)
			a_inte=np.random.choice(np.arange(0,11),5,replace=False)
			children[i]=after_fitness[first1]
			children[i+1]=after_fitness[second2]
			for j in a_inte:
				children[i][j] = after_fitness[second2][j]
				children[i+1][j] = after_fitness[first1][j]
				
			f=1
			if (children[i].tolist()==after_fitness[first1].tolist() or children[i].tolist()==after_fitness[second2].tolist() or children[i+1].tolist()==after_fitness[first1].tolist() or children[i+1].tolist()==after_fitness[second2].tolist()):
				f=0
		i+=2
	
	return children

def mutation(children):
	for i in range(children.shape[0]):
		temp=children[i]
		for j in range(11):
			temp[j]=np.random.uniform(-1.5,1.5)*temp[j]
		temp=np.clip(temp,-10,10)
		children[i]=temp
	return children

def mutation2(children):
	temp=children
	for j in range(11):
		temp[j]=np.random.uniform(-2.5,2.5)*temp[j]
	temp=np.clip(temp,-10,10)
	children=temp
	return children

pop_size=16
gen = np.zeros((pop_size,11))

# for i in range(pop_size):
# 	temp=overfit
# 	for j in range(11):
# 		temp[j]=np.random.uniform(-0.001,0.001)*temp[j]
# 	temp=np.clip(temp,-10,10)
# 	gen[i]=temp

for i in range(pop_size):
	gen[i]=mutation2(np.array(overfit))

fitness_value=np.zeros((gen.shape[0],3))
fitness_value=fitness(gen)

original_stdout=sys.stdout
for i in range(generations):
	fitness_value2=np.zeros((gen.shape[0],3))
	fitness_value2=fitness_value
	with open('gen_11.txt', 'a') as f:
		sys.stdout = f # Change the standard output to the file we created.
    

		print("Generation ")
		print(i+1)
		# print(fitness_value)
		print("initial")
		print("-----------------------")
		print(gen)
		# sys. stdout = open("output.txt", "a")
		
		# sys. stdout. close()
		print("after_fitness")
		print("-----------------------")
		after_fitness=selection(gen,fitness_value,i)
		print(after_fitness)
		if(i==generations-1):
			break
		print("after crossover")
		print("-----------------------")
		children=crossover(after_fitness)
		print(children)
		print("after mutation")
		print("-----------------------")
		children=mutation(children)
		print(children)

		fitness_value=fitness(children)
		# print(fitness_value)
		arr1 = np.concatenate((children, fitness_value), axis=1)
		arr2 = np.concatenate((gen, fitness_value2), axis=1)
		
		arr1=arr1[arr1[:,12].argsort()]
		arr2=arr2[arr2[:,12].argsort()]
		arr3= np.concatenate((arr1[2:pop_size], arr2[2:pop_size]), axis=0)
		arr3=arr3[arr3[:,12].argsort()]


		fitness_value[0:2,0:3]=arr1[0:2,11:14]
		fitness_value[2:4,0:3]=arr2[0:2,11:14]
		fitness_value[4:pop_size]=arr3[0:pop_size-4,11:14]

		gen[0:2,:]=arr1[0:2,0:11]
		gen[2:4,:]=arr2[0:2,0:11]
		gen[4:pop_size]=arr3[0:pop_size-4,0:11]
		sys.stdout = original_stdout # Reset the

with open('gen_11.txt', 'a') as f:
	sys.stdout=f
	print("vectors----------------------")
	final2=np.array(final)
	final2=final2[final2[:,11].argsort()]
	final2=final2[:,0:11]
	print(list(final2))
	sys.stdout = original_stdout

# final2=np.array(final)
# final2=final2[final2[:,11].argsort()]
# final2=final2[:,0:11]
# print(list(final2))

