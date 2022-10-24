def separar_lista():
    lista=[1,2,3,4,6,5,7,8,9]
    lista.sort()
    print(lista)
    lista_pares=[]
    lista_impares=[]
    for i in range (0,1,len(lista)):
        if lista[i]%2==0:
            aux=lista[i]
            lista_pares.append(aux)
        else:
            aux=lista[i]
            lista_impares.append(aux)
    return lista_pares, lista_impares


def main():
    lista=[1,2,3,4,5,6,7,8,9]
    x,y=separar_lista()
    print(x,y)



main()