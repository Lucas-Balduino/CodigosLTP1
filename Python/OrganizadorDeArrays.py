import array

def arrumaArray(array):
    i = 0
    for i in range(len(array)):
        j = i + 1
        for j in range(len(array)):
            if array[i] < array [j]:
                array[i], array[j] = array[j], array[i]
            j += 1
            print(array)
        i += 1
    return array

tamanhoArray = int(input('Digite o tamanho do array: '))

i = 0

print(f'Digite {tamanhoArray} numeros aleatorios')

array = array.array('i', [])

while tamanhoArray > i:
    numeroArray = (int(input(f'Digite o numero do index [{i}]')))
    array.append(numeroArray)
    i += 1

print(arrumaArray(array))

