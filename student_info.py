Student_info = {}

while True:
    while True:
        print("1. 학생 정보 추가")
        print("2. 학생 정보 검색")
        print("3. 학생 정보 삭제")
        print("4. 종료")
        Menu_input = int(input("메뉴에 대한 번호를 선택하세요 : "))

        if(Menu_input > 4 or Menu_input <= 0):
            print("메뉴에 해당되는 번호를 입력해주세요")
    
        break

    if(Menu_input == 1):
        name = input("이름 : ")
        student_ID = int(input("학번 : "))
        score = int(input("성적 : "))
        Student_info[student_ID] = name, score
    elif(Menu_input == 2):
        A = input("학번을 입력하시오 : ")
        print(Student_info[A])
    elif(Menu_input == 3):
        B = int(input("학번을 입력하시오 : "))
        del Student_info[B]
    else:
        break