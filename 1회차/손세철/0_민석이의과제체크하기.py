import sys
sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

for tc in range(1, T + 1) :
    n, k = map(int, input().split())
# 각 테스트 케이스마다 input된 k 개수 저장
    list_ = list(map(int, input().split()))
    result = []

# 1 ~ n+1 까지 반복문의 범위로 설정. i가 ㅣist_에 없다면 result에 i추가
    for i in range(1, n + 1) :
        if i not in list_ :
            result.append(i)

    print(f'#{tc}', *result)



