import sys
import math
import numpy as np
# from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import LogNorm
from matplotlib.pylab import *
from mpl_toolkits.axes_grid1 import host_subplot

plt.style.use('seaborn-pastel')

# Sent for figure
font = {'size'   : 12}
matplotlib.rc('font', **font)
error = []

def loss(pos, data):
	global X
	totalLoss = 0
	totalLoss = np.sum(np.square(data - (pos[0]*X + pos[1])))
	return np.sqrt(totalLoss/len(data))


def generate_data(n,mu,sigma,M,C):
	rand = np.random.normal(mu,sigma,(n,))
	X = np.linspace(1,n,n)
	model = M*X + C
	return model + rand

def update(i):
	global data, error, line2, line3


	# f = loss(particles[k].position[-1], data)



	# lines[-1].set_data(time, error)
	time = np.linspace(1,i+2,i+2)
	error.append(0.1)
	# print(time, np.asarray(error))
	line2.set_data(time, np.asarray(error))

	# line3.set_data(np.array([0, 500]), np.array([g_position[1], g_position[0]*500+g_position[1]]))

	return line2, line3



if __name__ == "__main__":

	n,mu,sigma,M,C = 100,0,100,25,120
	X = np.linspace(1,n,n)
	data = generate_data(n,mu,sigma,M,C)
	fig = plt.figure(figsize=(5,5))
	ax2 = subplot2grid((2,1),(0,0))
	line2, = ax2.plot([],[],lw=1)
	ax3 = subplot2grid((2,1),(1,0))
	line3, = ax3.plot([],[],lw=1)
	ax3.scatter(np.linspace(1,n,n), data, s=2)
	ax2.set_xlim(0,400)
	ax2.set_ylim(0,500)
	ax2.set_xlabel("Iterations Elapsed (RANSAC)")
	ax2.set_ylabel("Total Residual (RANSAC)")
	ax3.set_xlabel("X-axis (Independent Variable)")
	ax3.set_ylabel("Y-axis (Dependent Variable)")
	ax2.grid(True)
	ax3.grid(True)
	simulation = FuncAnimation(fig, update, blit=False, frames=2000, interval=100, repeat=False)
	plt.show()
