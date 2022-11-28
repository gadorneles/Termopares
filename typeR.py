import matplotlib.pyplot as plt
import numpy as np

temp = [0]*601
p = 0
for i in range(0,601):
    temp[i] = p
    p = p + 0.5

R_coef = [0, 0.528961729765E-02, 0.139166589782E-04, -0.238855693017E-07, 0.356916001063E-10, -0.462347666298E-13, 0.500777441034E-16, -0.373105886191E-19, 0.157716482367E-22, -0.281038625251E-26]
sum = 0
E= [0]*601

for i in range(0,601):
    for j in range(0,9):
      sum = sum + (R_coef[j]*(temp[i])**j)
    E[i] = sum
    sum = 0

print(E[600])
plt.plot(temp, E)
plt.xlabel('Temperature T (deg C)')
plt.ylabel('E(T) (mv)')
plt.title('Termopar Tipo R')
plt.show()