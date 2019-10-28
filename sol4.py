import numpy as np
import matplotlib.pyplot as plt

def isPareto(index, X):
    for i, vec in enumerate(X):
        if i != index and not np.any(X[index, :] > vec):
            return False
    return True

N = 10
M = 5
X = np.trunc(np.random.rand(N, M) * 10)
pareto = np.ndarray(0, dtype = int)
notpareto = np.ndarray(0, dtype = int)
for index in range(X.shape[0]):
    if isPareto(index, X):
        pareto = np.append(pareto, index)
    else:
        notpareto = np.append(notpareto, index)

fig, axes = plt.subplots(ncols=2, subplot_kw=dict(polar=True))
angle = 2 * np.pi * np.arange(0, 1 + 1 / M, 1 / M)
for i in pareto:
    axes[0].plot(angle, np.append(X[i], X[i, 0]))

for i in notpareto:
    axes[1].plot(angle, np.append(X[i], X[i, 0]))
    
plt.show()
