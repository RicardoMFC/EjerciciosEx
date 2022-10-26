import sys

def lista():
    cadena="Un día el viento soplaba con fuerza#mira cómo se mueve aquella banderola - dijo un monje#lo que se mueve es el viento - respondió otromonje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes - dijo el maestro"
    aux=[]
    aux2=[]
    #aux=cadena.replace('#','\n')
    j=0
    for i in range(len(cadena)):
        if cadena[i]=='#':
            
            #cadena.insert(i-1,".")
            aux=cadena.replace('#','.\n-')
            aux.replace(i+1,aux.upper())
            

            
    return aux

def main():
    list=lista()
    print(list)
main()



