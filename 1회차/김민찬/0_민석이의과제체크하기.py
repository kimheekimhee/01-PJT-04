import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())
for i in range(1, T + 1):
    N, K = map(int, input().split()) # 수강생의 수 = N, 과제 제출한 사람의 수 = K
    submit = list(map(int, input().split())) # 케이스마다 입력받은 K개의 수를 submit 리스트에 저장
    result = []

    for j in range(1, N + 1): # 1부터 N + 1까지의 반복문의 범위를 설정
        if j not in submit: # submit 리스트에 없다면
            result.append(j) # result 리스트에 j를 추가

    print(f'#{i}', *result) # [] 제거하기 위해 * 사용