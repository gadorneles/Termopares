import matplotlib.pyplot as plt
import numpy as np

temp = [0]*601
p = 0
for i in range(0,601):
    temp[i] = p
    p = p + 0.5

J_coef = [0, 0.503811878150e-1, 0.304758369300e-4, -0.856810657200e-7, 0.132281952950e-9, -0.170529583370e-12, 0.209480906970e-15, -0.125383953360e-18, 0.156317256970e-22]
sum = 0
E= [0]*601

for i in range(0,601):
    for j in range(0,8):
      sum = sum + (J_coef[j]*(temp[i])**j)
    E[i] = sum
    sum = 0

print(E[600])
plt.plot(temp, E)
plt.xlabel('Temperature T (deg C)')
plt.ylabel('E(T) (mv)')
plt.title('Termopar Tipo J')
plt.show()