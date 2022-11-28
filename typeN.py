import matplotlib.pyplot as plt
import numpy as np

temp = [0]*601
p = 0
for i in range(0,601):
    temp[i] = p
    p = p + 0.5

N_coef = [0, 0.259293946010e-1, 0.157101418800e-4, 0.438256272370e-7, -0.252611697940e-9, 0.643118193390e-12, -0.100634715190e-14, 0.997453389920e-18, -0.608632456070e-21, 0.208492293390e-24, -0.306821961510e-28]
sum = 0
E= [0]*601

for i in range(0,601):
    for j in range(0,10):
      sum = sum + (N_coef[j]*(temp[i])**j)
    E[i] = sum
    sum = 0

print(E[420])
plt.plot(temp, E)
plt.xlabel('Temperature T (deg C)')
plt.ylabel('E(T) (mv)')
plt.title('Termopar Tipo N')
plt.show()