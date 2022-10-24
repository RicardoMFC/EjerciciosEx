def separar_lista():
    lista=[1,2,3,4,6,5,7,8,9]
    lista.sort()
    print(lista)
    lista_pares=[]
    lista_impares=[]
    for i in range (len(lista)):
        aux=lista[i]
        if aux%2==0:
            lista_pares.append(aux)
        else:
            lista_impares.append(aux)
    return lista_pares, lista_impares


def main():
    x,y=separar_lista()
    print(x,y)
main()