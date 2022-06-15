# LIBRARIES
import math # Defecto
import scipy.stats as st # pip install scipy

# INPUTS
w18 = 900000
R = 0.8
Zr = st.norm.ppf(1-R)
S0 = 0.35
psi = 2.1
pt = 2
Sc = 615
Cd = 1
J = 3.2
Ec = 3600000
k = 64
D = 20
error = 0.0001

# PROCESS
f = Zr*S0 + 7.35*math.log(D+1,10) - 0.06 + math.log(psi/(4.5-1.5),10)/(1+1.624*10**7/(D+1)**8.46) + (4.22-0.32*pt)*math.log((Sc*Cd*(D**0.75-1.132))/(215.63*J*(D**0.75-18.42/(Ec/k)**0.25)),10) - math.log(w18,10)

while abs(f) >= error:
	D = D - 0.00001
	f = Zr*S0 + 7.35*math.log(D+1,10) - 0.06 + math.log(psi/(4.5-1.5),10)/(1+1.624*10**7/(D+1)**8.46) + (4.22-0.32*pt)*math.log((Sc*Cd*(D**0.75-1.132))/(215.63*J*(D**0.75-18.42/(Ec/k)**0.25)),10) - math.log(w18,10)

# OUTPUTS
print("Error =",abs(f))
print("D =",round(D,2))
