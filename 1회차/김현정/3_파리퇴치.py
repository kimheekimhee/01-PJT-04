import sys

sys.stdin = open("_파리퇴치.txt")

# 테스트케이스 수 변수 선언
T = int(input())

# T 갯수만큼의 테스트케이스 처리
for h in range (1, T+1):

    # 파리개수 담는 배열 N, 파리채 크기 M 입력받음
    N, M = map(int, input().split())

    # 파리개수 담는 배열 N_list 정의
    N_list = [list(map(int, input().split())) for _ in range(N)]

    # 파리개수 총합을 담는 리스트 선언
    N_sum_list = []

    # 파리채로 파리 배열을 순회할 수 있는 최대의 수는 N-M+1
    # i, j는 파리 배열을 순회함
    for i in range(N-M+1):
        for j in range(N-M+1):

            # 파리 배열을 순회할 파리채 배열 선언
            M_sum = 0
            for m in range(i, i+M):
                for n in range(j, j+M):
                    # 파리채로 잡을 파리 합 구하기
                    M_sum += N_list[m][n]
            # 합을 다 구했다면 결과값 리스트에 추가
            N_sum_list.append(M_sum)

    # 파리채로 잡을 수 있는 "최대"의 파리 수 출력
    print(f"#{h}", max(N_sum_list))