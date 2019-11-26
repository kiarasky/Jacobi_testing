""" This code plots a solution matrix
    Author and license
"""

import matplotlib.pyplot as plt
import numpy as np

a = np.loadtxt("solution.dat")
plt.matshow(a)

plt.savefig('solution.png')
plt.show()
