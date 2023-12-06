import math
import numpy as np
import matplotlib.pyplot as plt

K2 = [ [59, -40],[40, -20], [-10,-40],  [-63, 24],[-31, 56],[-30, 25] , [52, 26]]
verticles = K2
verticles.append(verticles[0])
ox,oy = zip(*verticles)
plt.plot(ox,oy,'-xk', label='Range')
plt.show()
