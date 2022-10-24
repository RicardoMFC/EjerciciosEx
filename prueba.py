def listas():
    lista_1 = ['h','o','l','a',' ', 'm','u','n','d','o']
    lista_2 = ['h','o','l','a',' ', 'l','u','n','a']
    lista_aux=[]

    for i in range (len(lista_1)):
        for j in range(len(lista_2)):
            if lista_1[i]==lista_2[j] and lista_1[i]!=' ':
                if len(lista_aux)==0:
                    lista_aux.append(lista_1[i])
                else:
                    val=1
                    for k in range (len(lista_aux)):
                        if lista_aux[k]==lista_1[i]:
                            val=0
                    if val==1:
                        lista_aux.append(lista_1[i])
    print (lista_aux)
listas()