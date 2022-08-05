import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

for _ in range(T):
    N, K = map(int,input().split()) #N:전체인원, K:과제제출인원
    subm = list(map(int,input().split())) #과제 제출한 사람 번호
    # print(N, K, a)
    check_ = []
    for i in range(1,N+1): #전체출석부를 생성.
        check_.append(i)
    
    print(f'#{_+1}',*(set(check_) - set(subm))) #과제를 제출X = 전체 출석부 = 제출자