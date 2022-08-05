import heapq
import sys

sys.stdin = open("_조교의성적매기기.txt")
ssr = sys.stdin.readline

# 테스트 케이스의 개수 T
t = int(ssr)
# 빈 리스트 생성
heapq = []
for i in range(int(ssr)):
    t = int(ssr)
    # heapq의 길이가 0과 다르면
    if len(heapq) != 0:
        heapq.pop([0], end=" ") # heapq의 인덱스 0을 뺌
    else: # 아니면
        heapq.push() # heapq에 추가

print(heapq[0])

