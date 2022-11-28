import matplotlib.pyplot as plt
import numpy as np

temp = [0]*601
p = 0
for i in range(0,601):
    temp[i] = p
    p = p + 0.5

B_coef = [0, -0.246508183460e-3, 0.590404211710e-5, -0.132579316360e-8, 0.156682919010e-11, -0.169445292400e-14, 0.629903470940e-18]
sum = 0
E= [0]*601

for i in range(0,601):
    for j in range(0,6):
      sum = sum + (B_coef[j]*(temp[i])**j)
    E[i] = sum

print(E[200])
plt.plot(temp, E)
plt.xlabel('Temperature T (deg C)')
plt.ylabel('E(T) (mv)')
plt.title('Termopar Tipo B')
plt.show()