import matplotlib.pyplot as plt
import numpy as np

temp = [0]*601
p = 0
for i in range(0,601):
    temp[i] = p
    p = p + 0.5

E_coef = [0, 0.586655087100e-1, 0.450322755820e-4, 0.289084072120e-7, -0.330568966520e-9, 0.650244032700e-12, -0.191974955040e-15, -0.125366004970e-17, 0.214892175690e-20, -0.143880417820e-23, 0.359608994810e-27]
sum = 0
E= [0]*601

for i in range(0,601):
    for j in range(0,10):
      sum = sum + (E_coef[j]*(temp[i])**j)
    E[i] = sum

print(E[420])
plt.plot(temp, E)
plt.xlabel('Temperature T (deg C)')
plt.ylabel('E(T) (mv)')
plt.title('Termopar Tipo E')
plt.show()