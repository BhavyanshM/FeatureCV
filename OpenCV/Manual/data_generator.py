import numpy as np
import matplotlib.pyplot as plt

font = 12
plt.rcParams.update({'font.size': font})


f = open("data.txt", 'w+')

N = 20
n = 1000
mu = 0
sigma = 100
M = 0.5
C = 10
rand = np.random.normal(mu,sigma,(n,))
X = np.linspace(1,n,n)


# for m in range(1000):
# 	for c in range(1000):
		

for i in range(n):
	f.write('{0:.2f}'.format(rand[i]) + "\n")



# for k in range(N):
# 	i = np.random.randint(n)
# 	j = np.random.randint(n)





plt.figure(figsize=(8,8))
plt.scatter(X, (M*X + C)+rand, s=2, c='red')
plt.scatter(X, (M*X + C), s=0.1, c='blue')
plt.xlabel('X-axis', fontsize=font, color='red')
plt.ylabel('Y-axis', fontsize=font, color='red')
plt.show()