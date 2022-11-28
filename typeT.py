import matplotlib.pyplot as plt

temp = [0]*601
p = 0
for i in range(0,601):
    temp[i] = p
    p = p + 0.5

T_coef = [0, 0.387481063640E-01, 0.332922278800E-04, 0.206182434040E-06, -0.218822568460E-08, 0.109968809280E-10, -0.308157587720E-13, 0.454791352900E-16, -0.275129016730E-19]
sum = 0
E= [0]*601

for i in range(0,601):
    for j in range(0,8):
      sum = sum + (T_coef[j]*(temp[i])**j)
    E[i] = sum
    sum = 0

print(E[600])
plt.plot(temp, E)
plt.xlabel('Temperature T (deg C)')
plt.ylabel('E(T) (mv)')
plt.title('Termopar Tipo T')
plt.show()