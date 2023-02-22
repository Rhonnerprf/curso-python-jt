n = int(input("Número de datos = "))

x = []
y = []

for i in range(n):
    x.append(float(input("x"+str(i+1)+" = ")))

for i in range(n):
    y.append(float(input("y"+str(i+1)+" = ")))

def regresion_lineal(x, y):
    xy = []
    for i in range(len(x)):
        xy.append(x[i]*y[i])
    
    x2 = []
    for i in range(len(x)):
        x2.append(x[i]*x[i])

    m = (sum(x)*sum(y) - len(x)*sum(xy))/((sum(x))**2 - len(x)*sum(x2))
    b = (sum(y) - m*sum(x))/len(x)

    return m, b

m, b = regresion_lineal(x, y)

print("y = "+str(round(m, 4))+"x"+" + "+str(round(b, 4)))
print("f(25) =", round(m*25 + b, 2))