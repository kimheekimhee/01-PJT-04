import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())
for _ in range(1, T + 1):
    N, M = map(int, input().split())
    NN = [list(map(int, input().split())) for a in range(N)]
    largest_smash = 0
    for b in range(N - M + 1):
        for c in range(N - M + 1):
            smash = 0
            for d in range(M):
                for e in range(M):
                    smash += NN[b + d][c + e]
            if smash >= largest_smash:
                largest_smash = smash
    print(f'#{_} {largest_smash}')