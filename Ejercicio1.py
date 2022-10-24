lista=["h","o", "u", "y", "r", "e"]
#lista.reverse()
print (lista)

j=int(len(lista)/2)
for i in range (0,1,j-1):
    aux=lista[len(lista)-i-1]
    lista[len(lista)-i-1]=lista[i]
    lista[i]=aux
print(lista)
    
