import sys

sys.stdin = open('_암호생성기.txt')

# 8자리 암호. 8개숫자입력받음. 첫째숫자 1 감소 ->마지막으로. 다음첫째수는 2감소 ->마지막.... 다 하는게 한싸이클. 감소했을때 음수되면 0으로 유지, 이러나저러나 마지막이 0되면 프로그램종료. 이때값이 암호

for i in range(10):
    test_case = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

    password = list(map(int, input().split()))

    #암호 첫번째껄 -1 시켜서 맨뒤로 보내고  .. 대충
    while password[-1] != 0:
        for j in range(1, 6):               # 1~5 만큼 빼는게 한사이클인걸 나중에 알아서 오래걸렸음
            for i in range(8):
                if i == 0:
                    temp = password[i] - j                
                    password[i] = password[i + 1]               
                elif 1 <= i <= 6:
                    password[i] = password[i + 1]
                else:
                    if temp > 0:
                        password[i] = temp
                    else:
                        password[i] = 0
                        break
            if password[-1] == 0:
                break
                    
    print(f'#{test_case}', end = ' ')
    for i in password:
        print(i, end = ' ')
    print()
    # while password[-1] != 0:
    #     temp = 0
    #     password[]



    ## 잘돌아가는데 제출이나 sys를 통한 출력은 이상이 있음
    #왜지????????

    #테스트케이스 입력방식을 바꿨는데 이렇게 하는게 맞는건지 모르겠음 (변수를 안넣고 상수 10(txt파일의 테스트케이스개수)을 넣는게 맞는가 싶음)