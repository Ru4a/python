def Selection_sort(sort_list):
    n = len(sort_list)
    for i in range(n):
        for j in range(i,n-1):
            if sort_list[i] > sort_list[j+1]:
                tmp = sort_list[i]
                sort_list[i] = sort_list[j+1]
                sort_list[j+1] = tmp
    return sort_list

example_sort = [3,1,7,9,4,2]
result = Selection_sort(example_sort)
print(result)

