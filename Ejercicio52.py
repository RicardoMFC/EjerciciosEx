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
    lista=[]
    aux=0
    while numero!=0:
        x=numero%10
        lista.append(x)
        numero=numero/10

def salida_ceros(numero_converso):
    aux=numero_converso
    i=0
    while aux!=0:
        aux=int(aux/10)
        i+=1

    while numero_converso/10!=0:
        print("{}\n".format(str(numero_converso%10).zfill(i)))
        numero_converso=numero_converso/10






def main():
    numero=introducir_num()
    numero_converso=conversion_numero(numero)
    salida_ceros(numero_converso)
    
main()