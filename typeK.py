import matplotlib.pyplot as plt
import numpy as np
import math

temp = [0]*601
p = 0
for i in range(0,601):
    temp[i] = p
    p = p + 0.5

K_coef = [-0.176004136860e-01, 0.389212049750e-01, 0.185587700320e-04, -0.994575928740e-07, 0.318409457190e-09, -0.560728448890e-12, 0.560750590590e-15, -0.320207200030e-18, 0.971511471520e-22, -0.121047212750e-25]
sum = 0
E= [0]*601

for i in range(0,601):
    for j in range(0,9):
      sum = sum + (K_coef[j]*(temp[i])**j)
    E[i] = sum + (0.118597600000*(math.e)**(-0.118343200000e-3*((temp[i] - 0.126968600000e3)**2)))
    sum = 0

print(E[420])
plt.plot(temp, E)
plt.xlabel('Temperature T (deg C)')
plt.ylabel('E(T) (mv)')
plt.title('Termopar Tipo K')
plt.show()