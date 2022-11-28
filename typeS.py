import matplotlib.pyplot as plt
import numpy as np

temp = [0]*601
p = 0
for i in range(0,601):
    temp[i] = p
    p = p + 0.5

S_coef = [0, 0.540313308631E-02, 0.125934289740E-04, -0.232477968689E-07, 0.322028823036E-10, -0.331465196389E-13, 0.255744251786E-16, -0.125068871393E-19, 0.271443176145E-23]
sum = 0
E= [0]*601

for i in range(0,601):
    for j in range(0,8):
      sum = sum + (S_coef[j]*(temp[i])**j)
    E[i] = sum
    sum = 0

print(E[100])
plt.plot(temp, E)
plt.xlabel('Temperature T (deg C)')
plt.ylabel('E(T) (mv)')
plt.title('Termopar Tipo S')
plt.show()