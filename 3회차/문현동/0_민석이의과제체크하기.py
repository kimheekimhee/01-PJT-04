import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

for test_case in range(1, T + 1):
    no = []
    N, K = map(int, input().split())
    
    num = [*map(int, input().split())]
    
    for whoes_num in range(1, N + 1):
        if whoes_num not in num:
            no.append(str(whoes_num))
            
    print(f"#{test_case} {' '.join(no)}")