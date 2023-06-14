age = int(input("나이 : "))


while True:
    is_member = input("회원 정보에 대해 입력하시오(Y/N) : ")

    if is_member == "Y" or is_member == 'N':
        break
    
    print("잘못된 입력입니다. 다시 입력해주세요.")


if age >= 18 and is_member == 'Y':
    print("입장 가능")
else:
    print("입장 불가능")