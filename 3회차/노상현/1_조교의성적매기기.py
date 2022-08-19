import sys

sys.stdin = open("_조교의성적매기기.txt")


T = int(input())
grade = ['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']

for case in range(T):
    a, b = map(int, input().split()) 
    arr = []

