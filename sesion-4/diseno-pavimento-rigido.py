# LIBRARIES

import math # paquete por defecto

# INPUTS

w18 = float(input("W18 = "))
Zr = float(input("Zr = "))
S0 = float(input("S0 = "))
psi = float(input("Serviciabilidad inicial (PSI) = "))
pt = float(input("Serviciabilidad final (pt) = "))
Sc = float(input("Sc = "))
Cd = float(input("Cd = "))
J = float(input("J = "))
Ec = float(input("Ec = "))
k = float(input("k = "))
D = 20
error = 0.0001

# PROCESS

f = Zr*S0 + 7.35*math.log(D+1,10) - 0.06 + math.log((psi-pt)/(4.5-1.5),10)/(1+1.624*10**7/(D+1)**8.46) + (4.22-0.32*pt)*math.log((Sc*Cd*(D**0.75-1.132))/(215.63*J*(D**0.75-18.42/(Ec/k)**0.25)),10) - math.log(w18,10)

while abs(f) >= error:
	D = D - 0.00001
	f = Zr*S0 + 7.35*math.log(D+1,10) - 0.06 + math.log((psi-pt)/(4.5-1.5),10)/(1+1.624*10**7/(D+1)**8.46) + (4.22-0.32*pt)*math.log((Sc*Cd*(D**0.75-1.132))/(215.63*J*(D**0.75-18.42/(Ec/k)**0.25)),10) - math.log(w18,10)

# OUTPUTS

print("D =", round(D, 2))
