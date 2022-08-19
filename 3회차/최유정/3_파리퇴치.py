# import sys

# sys.stdin = open("_파리퇴치.txt")

N, M = map(int, input().split())
N_list = []
#N*N
for i in range(N):
    N_list.append(list(map(int,input().split())))
#M*M
M_list = [[0]*M for m in range(M)]

#N*N을 돌면서 M*M에 숫자넣기
for i in range(N):
    for j in range(N):
        #N*N크기 만큼 합구하기
        #가장 큰 값 프린트

#print(M_list)
