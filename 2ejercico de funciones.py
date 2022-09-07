def mayormenor(lista):
    may=lista[0]
    men=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>may:
            may=lista[x]
        else:
            if lista[x]<men:
                men=lista[x]
    print("El valor mayor ingresado de la lista es", may)
    print("El valor menor ingresado de la lista es", men)          


lista=[]
for x in range(5):
    valor=int(input("Ingrese un valor:"))
    lista.append(valor)
mayormenor(lista)
