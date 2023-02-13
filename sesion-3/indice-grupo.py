'''
calcula el indice de grupo (IG) de la clasificación de suelos AASHTO
ingresar todos los datos numericos en valores enteros
F : % que pasa el tamiz #200
LL: límite líquido
IP: índice de plasticidad
claIG: calificación como subrasante a partir del indice de grupo
IG = 0, si el suelo se clasifica como A-1-a, A-1-b, A-2-4, A-3, A-2-5 
IG = 0.01 (F-15)*(IP-10), si el suelo se clasifica como A-2-6 o A-2-7. si IG < 0 asuma IG = 0
IG = (F-35)*(0.2+0.005*(LL-40))+0.01*(F-15)*(IP-10), otros suelos (A-4, A-5, A-6, A-7-5, A-7-6)   
IG = 0, subrasante excelente
IG >= 20, subrasante muy pobre
0 < IG < 20, subrasante regular (criterio particular, no lo indica la norma)
'''
# POR CORREGIR: ingreso de minusculas genera error (ejemplo: a-4), ingreso de AASHTO incorrecto (ejemplo: A-7) genera error. IDEA: considere los casos en minúscula. Podría hacerlo de cualquiera de las dos formas, por ejemplo: AASHTO == "a-1-a" o AASHTO = "A-1-a".lower().
# POR AGREGAR: si el suelo se identifica como "no plástico" según ASTM D4318, entonces IG=0
  
# ENTRADAS
AASHTO = input("tipo de suelo = ")
plasticidad = input("¿Suelo plástico (P) o no plástico (NP)?: ")
if plasticidad == "P":
    F = int(input("% que pasa el tamiz #200 = "))
    LL = int(input("límite líquido = "))
    IP = int(input("índice de plasticidad = "))

    # PROCESO
    if AASHTO == "A-1-a" or AASHTO == "A-1-b" or AASHTO == "A-2-4" or AASHTO == "A-3" or AASHTO == "A-2-5" or plasticidad == "NP":
        IG = 0
    elif AASHTO == "A-2-6" or AASHTO == "A-2-7": 
        F = int(input("% que pasa el tamiz #200 = "))
        IP = int(input("índice de plasticidad = "))
        IG = 0.01 * (F - 15) * (IP - 10)
        if IG < 0:
            IG = 0
    else:
        if AASHTO == "A-4" or AASHTO == "A-5" or AASHTO == "A-6" or AASHTO == "A-7-5" or AASHTO == "A-7-6" or AASHTO == "A-7":
            IG = (F - 35) * (0.2 + 0.005 * (LL - 40)) + 0.01 * (F - 15) * (IP - 10)
            if IG < 0:
                IG = 0

    # SALIDAS
    print ()
    if IG == 0:
        claIG = "excelente"
    elif IG >= 20:
        claIG = "muy pobre" 
    else:
        claIG = "regular"          

    print ('AASHTO\tF(%)\tLL\tIP\tIG\tclaIG')
    print ('-'*50)
    print (AASHTO,F,LL,IP,int(round(IG,0)),claIG,sep = '\t')
elif plasticidad == "NP":
    IG = 0
    print("IG =", IG)