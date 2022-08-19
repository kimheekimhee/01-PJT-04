import sys

sys.stdin = open("_파리퇴치.txt")

# 피드 참고 수정
test_case = int(input())

for test in range(1, test_case + 1):
    length, hit = map(int, input().split())
    seet = []
    for _ in range(length):
        line = list(map(int, input().split()))
        seet.append(line)

    most = 0
    for i in range(length - hit + 1):
        for j in range(length - hit + 1):
            fly = 0
            for i2 in range(hit):
                for j2 in range(hit):
                    fly += seet[i + i2][j + j2]
            if fly > most:
                most = fly

    print(f'#{test} {most}')




# test_case = int(input())

# for test in range(1, test_case + 1):
#     length, hit = map(int, input().split())
#     seet = []
#     for _ in range(length):
#         line = list(map(int, input().split()))
#         seet.append(line)
#     # 첫번째로 주어진 수를 한 변의 길이로 하는 2차원 면을 순회하는 작은 2차원 면 안의 값이 가장 큰 것을 찾는 방식을 택했습니다.

#     max = 0
#     # 최대로 잡은 값을 저장해줄 변수를 지정해줍니다.
#     for i in range(length - hit + 1):
#         for j in range(length - hit + 1):
#             # 주어진 매트릭스는 length * length 크기인데 인덱스 1만큼 움직이면서 안의 값 합이 가장 큰 hit * hit를 구할것이기 때문에 
#             # 범위는 length - hit + 1을 각 행열을 순회합니다.
#             fly = 0
#             # 이 때 매번 잡은 파리의 수를 저장할 변수를 지정해줍니다.
#             for i2 in range(hit):
#                 for j2 in range(hit):
#                     # hit의 크기만큼 행, 열을 순회하며 값들을 더하여 fly에 더해줍니다.
#                     fly += seet[i + i2][j + j2]
#             if fly > max:
#                 max = fly
#             # fly와 max를 비교하여 fly가 크면 max를 갱신하여 줍니다.

#     # 모든 반복이 끝나면 최댓값을 확인 할 수 있습니다.
#     print(f'#{test} {max}')