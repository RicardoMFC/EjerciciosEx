import math
def introducir_num():
    try:
        numero_usuario = int (input("Introduzca un número\n"))
        while numero_usuario<0:
            numero_usuario = int (input("Introduzca un número\n"))

    except:
        pass
    else:
        return numero_usuario

def conversion_numero(numero):
    aux=0
    while numero!=0:
        if numero>=10:
            aux=((numero%10) + aux)*10
        elif numero<10:
            aux=aux+(numero%10)
        numero=int(numero/10)
    return aux

def salida_ceros(numero_converso):
    aux=numero_converso
    i=0
    while aux!=0:
        aux=int(aux/10)
        i+=1
    print(i)
    j=0
    while numero_converso!=0:
        x=(numero_converso%10)*pow(10,j)
        print("{}\n".format(str(x).zfill(i)))
        numero_converso=int(numero_converso/10)
        j+=1

def main():
    numero=introducir_num()
    numero_converso=conversion_numero(numero)
    salida_ceros(numero_converso)
    
main()