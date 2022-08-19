import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())
for i in range(1, T+1):
    N , K = map(int, input().split())
    ratio = N//10
    grades = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    total_list = []
    for x in range(1, N+1):
        mid , finals , assign = map(int, input().split())
        total = mid * 35/100 + finals * 45/100 + assign * 20/100
        total_list.append(total)
    k_score = total_list[K-1]
    total_list.sort(reverse=True)
    final_k_score = total_list.index(k_score) // ratio
    print(f'#{i} {grades[final_k_score]}')
    