import sys
sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())
for tc in range(1, T+1):
    student = []
    a, b = map(int, input().split()) # 5 3
    number = list(map(int, input().split())) # [2, 5, 3]
    set(number)
    for i in range(1, a+1):
        student.append(i)
        set(student)
    set_ = set(student) & set(number)
    answer = list(map(str, set(student) - set_))    
    print(f"#{tc} {' '.join(map(str,answer))}") 