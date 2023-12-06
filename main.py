import math
import numpy as np
import matplotlib.pyplot as plt
 
# lấy giá trị góc tạo bởi 3 điểm
def getAngel(left,center,right):
    ang = math.degrees(math.atan2(center[1]-left[1], center[0]-left[0]) - math.atan2(right[1]-center[1], right[0]-center[0]))
    return ang + 360 if ang < 0 else ang

# chạy hết toàn bộ đỉnh để lấy góc
def checkAngel(ver):
    angel = []
    for i in range(len(ver)-1):
        if i == len(ver)-2:
            angel.append(getAngel(ver[i],ver[i+1],ver[1]))
        else:
            angel.append(getAngel(ver[i],ver[i+1],ver[i+2]))
    return angel
    
K2 = [ [59, -40],[40, -20], [-10,-40],  [-63, 24],[-31, 56],[-30, 25] , [52, 26]]

verticles = K2
verticles.append(verticles[0])

angel = checkAngel(ver=verticles)
print(angel)
ox,oy = zip(*verticles)
plt.plot(ox,oy,'-xk', label='Range')
plt.show()
