# LIBRARIES

import math

w18 = float(input("W18 = "))
Zr = float(input("Zr = "))
S0 = float(input("S0 = "))
psi = float(input("Serviciabilidad inicial (PSI) = "))
pt = float(input("Serviciabilidad final (pt) = "))
Mr = float(input("Mr = "))
SN = 10
error = 0.0001

# PROCESS

f = Zr*S0 + 9.36*math.log(SN+1,10) - 0.20 + math.log((psi-pt)/(4.2-1.5),10)/(0.4+1094/(SN+1)**5.19) + 2.32*math.log(Mr,10) - 8.07 - math.log(w18,10)

while abs(f) >= error:
    SN = SN - 0.00001
    f = Zr*S0 + 9.36*math.log(SN+1,10) - 0.20 + math.log((psi-pt)/(4.2-1.5),10)/(0.4+1094/(SN+1)**5.19) + 2.32*math.log(Mr,10) - 8.07 - math.log(w18,10)

# OUTPUTS

print("SN =", round(SN,2))