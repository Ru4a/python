def extract_odd_numbers(numbers):
    list_a_odd = []
    for i in numbers:
        if i % 2 != 0:
            list_a_odd.append(i)
    return list_a_odd

list_a = [10,7,6,5,9]
result = extract_odd_numbers(list_a)
print(result)
