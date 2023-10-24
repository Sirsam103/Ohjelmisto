def lispar(lista):
    parilliset=[]
    for i in lista:
        if i % 2 == 0:
            parilliset.append(i)
    return parilliset


lis = [3, 2, 15, 7, 4, 2, 9, 8, 4, 12, 3]
print(lis, lispar(lis))