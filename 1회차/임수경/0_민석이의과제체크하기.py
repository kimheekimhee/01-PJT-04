import sys

sys.stdin = open("_민석이의과제체크하기.txt")

#각 테스트 케이스마다 과제를 제출하지 않은 사람의 번호를 오름차순으로 출력
#오름차순으로 sort 라는 함수가 생각이 났고 
#계속해서 풀었왔던 실습문제 중에 오름차순으로 절렬 후 그 중에서 맨뒤에서 세번째로 큰 값을 출력하는 문제가 생각났습니다. 

#그렇다면, 본 문제를 어떻게 풀어나가면 좋을지 생각해 보았습니다. 
#처음에 for문으로 돌아 입력값에 해당 번호가 없다면 output를 해주면 되지 않을까 하는 접근 방법을 생각해보았습니다. 
#문제에서 더 지켜봐야하는 건 두번째 줄에서 과제를 제출한 사람의 번호 k개가 공백으로 구분되어진다고 한 점입니다. 
#수강생 수가 n명이고 제출한 사람이 k 명이라고 지정해줍니다. 

# 첫번째 오류 ValueError: too many values to unpack (expected 2) 오류 발생하여 코드를 다시 작성했습니다. 
# => result = list(map(int, input().split())) 이 코드 부분이 빠져서 오류가 생긴 것 같습니다. 

#두번째 문제 ) 두번째 줄 출력 이 0, 1, 2 번째만 나오고 있는 상태 
#1 1 2
#2 1 2
#어디가 잘못된 부분인지 몰라서 시간을 많이 소요 하였습니다. 

# T = int(input())

# for tc in range(1, T+1):
#     n, k = map(int, input().split())
#     result = list(map(int, input().split()))
#     result = []

#     for i in range(1, T+1):
#         if i not in result:
#             result.append(i)
#     print(f'#{tc}', *result)

#     # for i in range(1, n + 1) :
#     #     if i not in data :
#     #         result.append(i)

#     # print(f'#{tc}', *result)




T = int(input())
for tc in range(1,1+T):
 # n 수강생 수, k 제출한 사람 수
    n,k = map(int,input().split())
    # 제출한 사람의 번호
    submitted = list(map(int,input().split()))
    
    # 제출 안 한 사람 저장소
    no_submitted = []
 
    for q in range(1,n+1):
        if q not in submitted:
            no_submitted.append(q)
 
    print('#{}'.format(tc),*no_submitted)