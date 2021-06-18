def evaluacion():
    p1 = float(input())
    p2 = float(input())
    parcial1 = p1 * 0.25
    parcial2 = p2 * 0.25
    parciales = parcial1 +parcial2
    #### parcial 1 y 2 pesan el 25 %
    t = float(input())
    taller = t * 0.20
    
    p = float(input())
    pro = p * 0.30
    
    final = parciales + taller + pro
    
    acumulado = final

    print(final)
evaluacion()

    