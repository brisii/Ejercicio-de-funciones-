def crear_lista():
    li=[]
    for x in range(5):
        valor=int(input("Ingrese valor:"))
        li.append(valor)
    return li


def imprimir_mayor10(li):
    print("Elementos de la lista mayores a 12")
    for x in range(len(li)):
        if li[x]>12:
            print(li[x])


lista=crear_lista()
imprimir_mayor10(lista)
