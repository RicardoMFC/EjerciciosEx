def agregar_una_vez(lista, elemento):
    val=1
    for i in range (len(lista)):
        if elemento==lista[i]:
            val=0
            assert(elemento==lista)
    if val==1:
        lista.append(elemento)
    return lista

def main():
    lista=list("Hola que haces")
    elemento="H"
    lista=agregar_una_vez(lista, elemento)
    print(lista)
main()