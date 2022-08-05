import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())


for test_case in range(1, T+1):
    N, K = map(int, input().split())

    list_ = [list(map(int, input().split())) for _ in range(N)]

    # print(list_)
    garo_ = 0
  
    for i in range(N):
        garo_list = []
        for j in range(N):
            # 끝에 도달했는데 흰색 부분인 경우
            if j == N-1 and list_[i][j] == 1:
                # 문자를 추가하고
                garo_list.append(1)
                if len(garo_list) == K:
                    garo_ += 1

            # 흰색 부분인 경우 문자 추가
            elif list_[i][j] == 1:
                garo_list.append(1)

            # 검은색 부분인 경우
            elif list_[i][j] == 0:
                # 이때까지의 길이가 K이면 추가
                if len(garo_list) == K:
                    garo_ += 1

                garo_list.clear()

    sero_ = 0

    for i in range(N):
        sero_list = []
        for j in range(N):
            # 끝에 도달했는데 흰색 부분인 경우
            if j == N-1 and list_[j][i] == 1:
                # 문자를 추가하고
                sero_list.append(1)
                if len(sero_list) == K:
                    sero_ += 1

            # 흰색 부분인 경우 문자 추가
            elif list_[j][i] == 1:
                sero_list.append(1)

            # 검은색 부분인 경우
            elif list_[j][i] == 0:
                # 이때까지의 길이가 K이면 추가
                if len(sero_list) == K:
                    sero_ += 1

                sero_list.clear()

    #print(garo_ , sero_)
    print(f'#{test_case} {garo_ + sero_}')