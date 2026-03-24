from cmath import inf

lista = [1,5,8,3,9,2,7]
lista.sort()

def normalize(list):
    max = 0
    min = 10000
    for num in list:
        if num > max:
            max = num
        if num < min:
            min = num

    out = []
    for num in list:
        out.append((num-min)/(max-min))
    out.sort()

    return out


print(lista)
print(normalize(lista))
