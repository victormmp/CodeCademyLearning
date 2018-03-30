def remove_duplicates(lista):
    result = []
    for i in lista:
        if i not in result:
            result.insert(0,i)
    return result

print remove_duplicates(range(16))