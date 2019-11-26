import matplotlib.pyplot as plt
import numpy as np

a = np.loadtxt("solution.dat")
plt.matshow(a)

plt.savefig('solution.png')
plt.show()
