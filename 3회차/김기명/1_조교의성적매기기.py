# 중간 0.35 기말 0.45 과제 0.2
#입력 중-기-과
#K번째학생 학점출력
# import sys
# sys.stdin = open('_조교의성적매기기.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split()) # 사람수와 알고싶은사람번호

    list_N = []
    for i in range(N):
        list_N.append(list(map(int, input().split())))
    
    sum_ = 0
    sum_list = []
    for i in range(N):
        for j in range(3):
            if j == 0 :
                sum_ += list_N[i][j] * 0.35
            elif j == 1:
                sum_ += list_N[i][j] * 0.45
            else:
                sum_ += list_N[i][j] * 0.2

        sum_list.append(sum_)
        sum_ = 0
    # 점수표까진 만들었는데. 리스트를 등수로 어떻게 바꿀까 / 정렬하고.. 원본리스트와 비교??

    rank = sorted(sum_list)[::-1]
    
    for i in range(N):
        for j in range(N):
            if rank[i] == sum_list[j]:
                sum_list[j] = i + 1
                break
    
    for i in range(1, N + 1):
        if sum_list[K - 1] <= N / 10:
            print(f'#{test_case} A+')
            break
        elif 2 * N / 10 >= sum_list[K - 1] > N / 10:
            print(f'#{test_case} A0')
            break
        elif 3 * N / 10 >= sum_list[K - 1] > 2 * N / 10:
            print(f'#{test_case} A-')
            break
        elif 4 * N / 10 >= sum_list[K - 1] > 3* N / 10:
            print(f'#{test_case} B+')
            break
        elif 5 * N / 10 >= sum_list[K - 1] > 4*N / 10:
            print(f'#{test_case} B0')
            break
        elif 6 * N / 10 >= sum_list[K - 1] > 5*N / 10:
            print(f'#{test_case} B-')
            break
        elif 7 * N / 10 >= sum_list[K - 1] > 6*N / 10:
            print(f'#{test_case} C+')
            break
        elif 8 * N / 10 >= sum_list[K - 1] > 7*N / 10:
            print(f'#{test_case} C0')
            break
        elif 9 * N / 10 >= sum_list[K - 1] > 8*N / 10:
            print(f'#{test_case} C-')
            break
        elif 10 * N / 10 >= sum_list[K - 1] > 9*N / 10:
            print(f'#{test_case} D0')
            break








