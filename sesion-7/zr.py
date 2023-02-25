import scipy.stats as st

R = float(input("R = "))
Zr = st.norm.ppf(1-R)

print("Zr =", Zr)