#https://www.acmicpc.net/problem/2512 문제 사이트

N = int(input())
M = 485
list_N = []
for i in range(N):
    value = int(input("값 : ")) #리스트에 정수형으로 저장
    list_N.append(value)


#리스트의 값에서 상한값을 찾음
def search_upper_bound(list_A):
    upper_bound = max(list_A)
    return upper_bound


#현재 high는 문자열로 되어 있다.
#int()를 통해 다시 정수형으로 바꿈
high = int(search_upper_bound(list_N))


def Calculate(N,M,list_A, high):
    low = 0 #Lower_upper
    #binary는 이분 탐색 값
    while low <= high: #이분 탐색에서 가장 핵심적인 부분
        result = 0
        binary = (low + high)//2
        for i in range(N):
            result += min(list_A[i],binary)
        print('하한값 : {}'.format(low))
        print('상한값 : {}'.format(high))
        print('결과 : {}' .format(result))

        if result > M:
            high = binary -1 #상한값 업데이트
            #마지막 결과값에서 1을 뺴줘서 상한값에 대한 값을 맞춤
        else:
            low = binary + 1#하한값 업데이트
    return high

result = Calculate(N, M, list_N, high)

print(result)


#정상적으로 결과 출력
#전체 국가 예산은 485로 고정이기에 변경

            


