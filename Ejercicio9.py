import sys

def modificar(lista):
    
    for i in range (0,len(lista),1):
        for j in range (0,len(lista),1):
            if lista[i]==lista[j] and i!=j:
                lista=lista.pop(j)

    return lista



def main():
    lista=list(1357924688)
    aux=modificar(lista)
    print(aux)
main()
