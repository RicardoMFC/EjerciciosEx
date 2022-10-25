from ast import Assert


def agregar_una_vez(lista, elemento):
    val=1
    for i in range (len(elemento)):
        for j in range (len(lista)):
            if elemento[i]==lista[j]:
                val=0
                assert(elemento==lista)
        if val==1:
            lista.append(elemento[i])

    return lista

def main():
    lista=list("Hola que haces")
    elemento=list("gtrh")
    lista=agregar_una_vez(lista, elemento)
    print(lista)
main()