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

# PROCESS

D = max(1.132 ** (1 / 0.75), (18.42 / (Ec / k) ** 0.25) ** (1 / 0.75)) + 0.0001
error = 0.0001
f = Zr * S0 + 7.35 * math.log10(D + 1) - 0.06 + math.log10((psi - pt) / (4.5 - 1.5)) / (1 + 1.624 * 10 ** 7 / (D + 1) ** 8.46) + (4.22 - 0.32 * pt) * math.log10((Sc * Cd * (D ** 0.75 - 1.132)) / (215.63 * J * (D ** 0.75 - 18.42 / (Ec / k) ** 0.25))) - math.log10(w18)

while abs(f) >= error:
    D = D + 0.0001
    f = Zr * S0 + 7.35 * math.log10(D + 1) - 0.06 + math.log10((psi - pt) / (4.5 - 1.5)) / (1 + 1.624 * 10 ** 7 / (D + 1) ** 8.46) + (4.22 - 0.32 * pt) * math.log10((Sc * Cd * (D ** 0.75 - 1.132)) / (215.63 * J * (D ** 0.75 - 18.42 / (Ec / k) ** 0.25))) - math.log10(w18)

# OUTPUTS

print("D =", round(D, 2))