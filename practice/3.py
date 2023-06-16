list_integer = [1,2,3,4,5,6,7,8,9,10]

def list_filter(list):
    list_A = []

    for i in list_integer:
        if i % 2 == 0:
            list_A.append(i)

    return list_A


result = list_filter(list_integer)
print(result)