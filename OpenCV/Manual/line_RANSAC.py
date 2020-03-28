import time
import numpy as np
import matplotlib.pyplot as plt

font = 12
plt.rcParams.update({'font.size': font})


f = open("data.txt", 'w+')

N = 20
n = 2000
mu = 0
sigma = 500
M = 3.7
C = 1000
rand = np.random.normal(mu,sigma,(n,))
rand2 = (np.random.random((n,))>0.98)*(np.random.randint(-5,6, size=(n,))*2000)
rand3 = (np.random.random((n,))>0.99)*(np.random.randint(-5,6, size=(n,))*4000)
print(rand2[:10])
X = np.linspace(1,n,n)
data = (M*X + C)+rand+rand2+rand3
m,c = 0,0
count = 0
model = 0,0
minLoss = 0


def inliers(model, data):
	global X
	totalLoss = 0
	totalLoss = np.square(data - (model[0]*X + model[1]))
	return np.sum(totalLoss<10000)


for i in range(n):
	f.write('{0:.2f}'.format(rand[i]) + "\n")

iteration = 0
t0 = time.time()
while True:
	x1 = np.random.randint(n)
	x2 = np.random.randint(n)
	consensus = 0
	if x1 < x2 :
		iteration += 1
		dy = data[x2] - data[x1]
		dx = x2 - x1
		m = dy/dx
		c = data[x1] - m*x1
		consensus = inliers((m,c),data)
		if count < consensus:
			count = consensus
			model = (m,c)
			print(iteration, m,c, count)
	if iteration > 10000:
		break
t1 = time.time()

print("\nTime Taken:", t1-t0, "secs")






plt.figure(figsize=(8,8))
plt.scatter(X, data, s=1, c='red')
plt.scatter(X, (model[0]*X + model[1]), s=0.1, c='blue')
plt.xlabel('X-axis', fontsize=font, color='red')
plt.ylabel('Y-axis', fontsize=font, color='red')
plt.show()