print("Questo programma trova la soluzione di una equazione di primo grado di tipo ax + b = 0.")
t_noto = float(input("Qual'è il valore noto 'b' ? "))
coef_x = float(input("Qual'è il valore di 'a', cioè il coefficiente della x ? "))

if coef_x == 0 :
    if t_noto == 0 :
        print("La soluzione è indeterminata 0x = 0")
    elif t_noto != 0:
        print("La soluzione è impossibile") 

elif  coef_x != 0 :
    if t_noto == 0 :
        print("La soluzione è x = 0")
    elif t_noto != 0:
        x = - ( t_noto / coef_x)
        print("La soluzione è x = -", t_noto, " / ", coef_x, ", cioè, x = ", x ) 
