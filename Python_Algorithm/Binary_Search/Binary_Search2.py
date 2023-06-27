#https://www.acmicpc.net/problem/1300 알고리즘 문제

N = int(input("N의 값 : "))
k = int(input("k의 값 : "))

A = [[0] * N for _ in range(N)]
#이 부분은 이중 리스트를 생성하는 코드다.
#[0]*N은 값이 0인 1차원 리스트를 생성하는 것
#[[0] * N]이 결과는 [[0,0,0]]이다.


for i in range(N):
    for j in range(N):
        A[i][j] = (i+1) * (j+1)
#인덱스(요소)가 1부터 시작
#요소 값을 대입하기 위한 코드5

X_min = A[0][0] #1
X_max = A[N-1][N-1] #25

num_case1 = k-1 #조건1
num_case2 = N*N - k #조건2


min_count = 0
max_count = 0
X = 0
while True:
    min_count = 0
    max_count = 0
    X = (X_min + X_max)//2 #초기 값 13
    for i in range(N):
        for j in range(N):
            if A[i][j] < X:
                min_count = min_count + 1
            elif A[i][j] > X:
                max_count = max_count + 1
    print(X_min)


    if min_count > num_case1: #조건1 위반
        X_max = X - 1 #num_case1 = 16
    elif max_count > num_case2: #조건2 위반
        X_min = X + 1 #num_case2 = 8

    if min_count <= num_case1 and max_count <= num_case2: #모든 조건을 만족했을 때 반복문 탈출
        print(X) #x값 출력
        break #조건 1 만족 and 조건2 만족

