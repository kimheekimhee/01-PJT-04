import sys
from pprint import pprint

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

input = sys.stdin.readline
T = int(input())

for i in range(T): # 테스트 케이스
    N, K = map(int,input().split()) # 배열크기, 단어길이
    matrix = [list(map(int,input().split())) for _ in range(N)]
    pprint(matrix)