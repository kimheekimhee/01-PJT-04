import sys
from pprint import pprint

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())

for test_case in range(1, T + 1):
    rank = []
    rating = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    
    N, K = map(int, input().split())
    
    for _ in range(N):
        m, f, a = map(int, input().split())
    
        total = (m * 0.35) + (f * 0.45) + (a * 0.2)
        rank.append(str(total))
        rank.sort(reverse = True)
