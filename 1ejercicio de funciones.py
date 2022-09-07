def presentacion():
    print("Programa que permita ingresar  dos valores por teclado.")
    print("Efectuar la suma de los valores")
    print("Muestra el resultado de la suma")
    print("*******************************")


def carga_suma():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    suma=valor1+valor2
    print("La suma de los dos valores es:",suma)


def finalizacion():
    print("*******************************")    
    print("Gracias por realizar la suma con nuestro programa")


# programa principal

presentacion()
carga_suma()
finalizacion()
