import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

# 피드 참고 수정
test_case = int(input())

for test in range(1, test_case + 1):
    size, length = map(int, input().split())
    
    seet = []
    for _ in range(size):
        line = list(map(int, input().split()))
        seet.append(line)
    
    right = 0
    for i in range(size):
        word = 0
        for j in range(size):
            if seet[i][j] == 1:
                word += 1
            else:
                if word == length:
                    right += 1
                word = 0

        if word == length:
            right += 1

    for i in range(size):
        word = 0
        for j in range(size):
            if seet[j][i] == 1:
                word += 1
            else:
                if word == length:
                    right += 1
                    word = 0
                else:
                    word = 0
        if word == length:
            right += 1
            
    print(f'#{test} {right}')



# 나의 풀이
# test_case = int(input())

# for test in range(1, test_case + 1):
#     size, length = map(int, input().split())
    
#     seet = []
#     for _ in range(size):
#         line = list(map(int, input().split()))
#         seet.append(line)
    
#     right = 0
#     # 원하는 길이의 단어가 들어갈 수 있으면 값을 추가해줄 변수를 지정해 줍니다.
#     for i in range(size):
#         word = 0
#         # 행을 순회하며 매 단어의 길이를 저장해줄 변수를 지정해 줍니다. 
#         for j in range(size):
#             # i 행을 순회하며 변화하는 j 열의 값을 확인하면 행을 순회하며 값들을 확인 할 수 있습니다.
#             if seet[i][j] == 1:
#                 word += 1
#                 # 자리의 값이 1이면 단어의 길이를 1 증가시킵니다.
#             else:
#                 # 값이 0과 1만 주어지기에 아닌 경우 0이 오게되니 else를 써도 괜찮아 보입니다.
#                 if word == length:
#                     right += 1
#                     word = 0
#                 else:
#                     word = 0
#                     # 단어의 길이가 원하는 길이면 right을 1 증가 시키고 word를 초기화시키고
#                     # 아니라면 그냥 word만 초기화를 시켜줍니다.
#         if word == length:
#             right += 1
#         # 반복이 끝날때 1로 끝나면 단어의 길이를 확인 못 하기 때문에 마지막에 한 번 더 단어의 길이를 확인해 줍니다.
#     #위의 반복을 통해 행을 순회하며 원하는 길이의 단어가 들어갈 수 있는지 확인해줍니다.

#     for i in range(size):
#         word = 0
#         for j in range(size):
#             if seet[j][i] == 1:
#                 word += 1
#             else:
#                 if word == length:
#                     right += 1
#                     word = 0
#                 else:
#                     word = 0
#         if word == length:
#             right += 1
#     # 위와 동일한 방법으로 열을 순회하며 원하는 길이의 단어가 들어갈 수 있는지 확인해주고 값을 추가해 줍니다.
#     # 행, 열에 각 몇개의 값을 원하는지가 아닌 총 갯수를 구하는 것이니 행에 구해준 값에 추가되는 값을 누적시켜 줍니다.
            
#     print(f'#{test} {right}')