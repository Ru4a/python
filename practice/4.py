str_A = 'qwqweekkmaa'

def Function1(str_Example):
    list_A = []
    counter = len(str_Example)
    for i in str_Example:
        list_A.append(i)

    result1 = None
    counter_A = 0


    for i in range(0,counter):
        for j in range(0,counter-1):
            print("i : {}".format(i))
            print("j : {}".format(j))
            if list_A[i] == list_A[j]:
                counter_A += 1
                print(counter_A)
        if counter_A == 1:
            return list_A[i]
        counter_A = 0    
    

    if result1 is None:
        result1 = '#'

    return result1

result = Function1(str_A)
print(result)