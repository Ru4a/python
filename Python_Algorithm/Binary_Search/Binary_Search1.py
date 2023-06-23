N = int(input())
M = int(input("최대 예산: "))
list_N = []
for i in range(N):
    value = int(input("값: "))  # 리스트에 정수형으로 저장
    list_N.append(value)

def search_upper_bound(list_A):
    upper_bound = max(list_A)
    return upper_bound

high = int(search_upper_bound(list_N))

def Calculate(N, M, list_A, high):
    low = 0
    result = 0  # 결과 변수 초기화
    while low <= high:
        binary = (low + high) // 2
        result = 0  # 반복할 때마다 결과 초기화
        for i in range(N):
            result += min(list_A[i], binary)
        print('하한값 : {}'.format(low))
        print('상한값 : {}'.format(high))
        print('결과 : {}' .format(result))
        if result > M:
            high = binary - 1
        else:
            low = binary + 1
    
    return high  # high 값을 반환하도록 수정

result = Calculate(N, M, list_N, high)
print(result)
