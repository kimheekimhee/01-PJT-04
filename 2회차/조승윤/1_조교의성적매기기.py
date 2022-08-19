import sys
from telnetlib import PRAGMA_HEARTBEAT

sys.stdin = open("_조교의성적매기기.txt")
t = int(input())
lst =[]
g = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for _ in range(1,t+1):
    n, m = map(int, input().split())
    for i in range(n):
        a, b, c = map(int, input().split())
        score = (a * 0.35) + (b * 0.45) + (c * 0.2)
        lst.append(score)
        
    t_lst = lst[m-1]
    lst.sort
    div = n//10
    k = lst.index(t_lst)//div
    print(f'#{_} {g[k]}')