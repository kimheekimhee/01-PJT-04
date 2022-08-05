import sys

sys.stdin = open("_민석이의과제체크하기.txt")

t = int(input())                                         # 정수를 입력 받는다

for tc in range(1, t + 1) :
    n, k = map(int, input().split())                     # 수강생 수 N과 과제 제출한 수강생 수 k 를 공백으로 구분
    data = list(map(int, input().split()))               # 각 테스트케이스마다 입력받은 k수를 data 리스트에 저장
    result = []

    for i in range(1, n + 1) :                           # i가 data 리스트에 존재하지 않는다면 result 리스트에 i를 추가
        if i not in data :
            result.append(i)

    print(f'#{tc}', *result)