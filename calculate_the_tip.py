print("¿Cual es el total de la cuenta?")
bill = float(input())
tip = [0.18, 0.20, 0.25]
for i in tip:
    txt = "Con un porcentaje del {:.1f}% la propina seria de ${:.2f} y un total de  ${:.2f}"
    print(txt.format(i*100, bill*i, bill*(1+i)))