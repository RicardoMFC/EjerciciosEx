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

def salida_ceros(numero):
    aux=numero
    i=0
    while aux!=0:
        aux=int(aux/10)
        i+=1
    print(i)
    j=0
    while numero!=0:
        x=(numero%10)*pow(10,j)
        print("{}\n".format(str(x).zfill(i)))
        numero=int(numero/10)
        j+=1

def main():
    numero=introducir_num()
    salida_ceros(numero)
    
main()