def maximo (n):
    k=[]
    x=0
    while x<n:
        palabra=input("Numero:"+str(x+1))
        k.append(palabra)
        x=x+1
    return k


n=int(input("Cantidad de numeros que desea ingresar en la lista: "))
lista=maximo(n)
print("La lista es:",lista)
print("El mayor numero de la lista es:")
print (max(lista))

       
