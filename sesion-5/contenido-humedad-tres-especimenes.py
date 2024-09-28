# ENTRADAS

pesos1 = [770.1, 1895.3, 1721.4]
pesos2 = [731.7, 2008.4, 1801.2]
pesos3 = [770.6, 1827.9, 1660.8]

# PROCESO

pesoAgua1 = pesos1[1] - pesos1[2]
pesoSolidos1 = pesos1[2] - pesos1[0]
contenidoHum1 = round((pesoAgua1/pesoSolidos1)*100)
pesoAgua2 = pesos2[1] - pesos2[2]
pesoSolidos2 = pesos2[2] - pesos2[0]
contenidoHum2 = round((pesoAgua2/pesoSolidos2)*100)
pesoAgua3 = pesos3[1] - pesos3[2]
pesoSolidos3 = pesos3[2] - pesos3[0]
contenidoHum3 = round((pesoAgua3/pesoSolidos3)*100)
contenidoHum = round((contenidoHum1 + contenidoHum2 + contenidoHum3)/3)

# SALIDA

print("Contenido de humedad (%) =", contenidoHum)