def median(lista):
    lista.sort()
    mediana=0
    if len(lista)%2 == 0:
       mediana = (lista[len(lista)//2 -1] + lista[len(lista)/2])/2.0
    else:
        mediana = lista[len(lista)//2]
    return mediana

print(median([1,2,3,4,5]))
