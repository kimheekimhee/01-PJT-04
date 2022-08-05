# import sys

# sys.stdin = open("_파리퇴치.txt")

# 강사님께서 오늘 알려주신 dx, dy를 활용해서 풀고 싶었는데, 오늘 막 배운 방법이라 익숙하지 않아 실수를 할까봐 그냥 for문으로 풀었습니다.
# for문을 4번이나 중첩하여 시간 복잡도가 O(N^4)인 것을 알고 있는데, 최대 값이 15이기에 15^4를 해도 50,625 번의 연산밖에 일어나지 않아 그 방법으로 풀었습니다.
# 나중에 dx,dy를 좀 더 공부하고 익힌 다음 그 방법으로 풀면 훨씬 더 빠르고 간편하게 풀 수 있을 것 같습니다.

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    list_ = [list(map(int, input().split())) for _ in range(N)]

    # 합을 저장할 리스트를 찾고
    sum_list =[]

    # 파리채의 크기가 M인 경우 list의 범위가 끝까지 가면 index를 넘어가므로
    # 가로 0부터 N-M까지
    for i in range(N-M+1):
        # 세로 0부터 N-M까지 
        for j in range(N-M+1):
            sum_ = 0
            # 파리채의 크기만큼의 값들을 전부 더한 후
            for k in range(M):
                for l in range(M):
                    sum_ += list_[i+k][j+l]
            # 합을 저장하는 list에 저장
            sum_list.append(sum_)
    # 합 중 최댓값 출력
    print(f'#{test_case} {max(sum_list)}')