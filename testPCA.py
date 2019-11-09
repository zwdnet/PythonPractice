# coding:utf-8


import numpy as np


def compute_pca(data):
	m = np.mean(data, axis = 0)
	datac = np.array([obs - m for obs in data])
	T = np.dot(datac, datac.T)
	[u, s, v] = np.linalg.svd(T)
	
	pcs = [np.dot(datac.T, item) for item in u.T]
	pcs = np.array([d/np.linalg.norm(d) for d in pcs])
	
	return pcs, m, s, T, u
	
	



if __name__ == "__main__":
	pass