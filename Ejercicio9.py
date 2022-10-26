import sys

def modificar(lista):
    for i in range (len(lista)):
        for j in range (len(lista)):
            if lista[i]==lista[j] and i!=j:
                lista[j]==' '
    print(lista)


def main():
    lista=[1,2,3,5,4,6,7,8,9,9]
    modificar(lista)

main()