import sys
sys.stdin = open("_파리퇴치.txt")
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    max_sum = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            M_sum = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    M_sum += matrix[k][l]
            if M_sum > max_sum:
                max_sum = M_sum

    print(f'#{t} {max_sum}')
# print(matrix[0][0]+matrix[0][1]+matrix[1][0]+matrix[1][1])
# print(matrix[0][1]+matrix[0][2]+matrix[1][1]+matrix[1][2])
# print(matrix[0][2]+matrix[0][3]+matrix[1][2]+matrix[1][3])
# print(matrix[0][3]+matrix[0][4]+matrix[1][3]+matrix[1][4])

# print(matrix[1][0]+matrix[1][1]+matrix[2][0]+matrix[2][1])
# print(matrix[1][1]+matrix[1][2]+matrix[2][1]+matrix[2][2])
# print(matrix[1][2]+matrix[1][3]+matrix[2][2]+matrix[2][3])
# print(matrix[1][3]+matrix[1][4]+matrix[2][3]+matrix[2][4])