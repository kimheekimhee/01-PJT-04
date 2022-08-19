import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())
for test_case in range(1, T+1):
    student = list(map(int, input().split()))
    number = set(map(int, input().split()))
    
    all_number = set()
    for a in range(1, student[0]+1):
        all_number.add(a)
    no_number = map(str, all_number - number)
    print(f"#{test_case} {' '.join(no_number)}")

