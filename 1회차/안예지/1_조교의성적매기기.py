import sys

# sys.stdin = open("_조교의성적매기기.txt")

"""
87 59 88
99 94 78
94 86 86
99 100 99
69 76 70
76 89 96
98 95 96
74 69 60
98 84 67
85 84 91
"""
from pprint import pprint
import heapq
N = 10
score = [[87, 59, 88],
        [99, 94, 78],
        [94, 86, 86],
        [99, 100, 99],
        [69, 76, 70],
        [76, 89, 96],
        [98, 95, 96],
        [74, 69, 60],
        [98, 84, 67],
        [85, 84, 91]]
# for row in range(N):
#     score.append(list(map(int, input().split())))
# pprint(score)
maxy = []
for r in range(N):
    maxy.append(sum(score[r]))
pprint(sorted(maxy))
maxy_n = heapq.heapify(maxy)
heapq.heappop(maxy)