import matplotlib.pyplot as plt
import typeE
import typeB
import typeJ
import typeN
import typeT
import typeR
import typeS
import typeK 

plt.plot(typeB.temp, typeB.E, label = "Tipo B")
plt.plot(typeE.temp, typeE.E, label = "Tipo E")
plt.plot(typeJ.temp, typeJ.E, label = "Tipo J")
plt.plot(typeN.temp, typeN.E, label = "Tipo N")
plt.plot(typeT.temp, typeT.E, label = "Tipo T")
plt.plot(typeR.temp, typeR.E, label = "Tipo R")
plt.plot(typeS.temp, typeS.E, label = "Tipo S")
plt.plot(typeK.temp, typeK.E, label = "Tipo K")

plt.xlabel('Temperature T (deg C)')
plt.ylabel('E(T) (mv)')
plt.legend()
plt.show()
